import json
import re
import ast
import http.client
import ssl
import concurrent.futures

def gpt_api(question, model):
    conn = http.client.HTTPSConnection("api.gptgod.online")
    payload = json.dumps({
        "model": model,
        "messages": [
            {
                "role": "system",
                "content":
                    "You are a professional Open-domain Question Answering assistant."
                    "You will generate an evidence that helps to match relevant passages and contexts with the given question."
                    "The evidence should be directly relevant to the question and should not include unnecessary details."
                    "Please make sure to strictly follow this format in your answer: ***evidence***, without any extra explanations.\n"
                    "Here is an example:\n"
                    "Question: who got the first nobel prize in physics?\n"
                    "your answer:***Röntgen received the first Nobel Prize in Physics for his discovery***\n"
            },
            {
                "role": "user",
                "content":
                # "You are a professional Open-domain Question Answering assistant."
                # "You will generate an evidence that helps to match relevant passages and contexts with the given question."
                # "The evidence should be directly relevant to the question and should not include unnecessary details."
                # "Please make sure to strictly follow this format in your answer: ***evidence***, without any extra explanations.\n"
                # "Here is an example:\n"
                # "Question: who got the first nobel prize in physics?\n"
                # "your answer:***Röntgen received the first Nobel Prize in Physics for his discovery***\n"
                # "Next is question:"
                    f"question: {question}\n"

            }
        ],
        "stream": False,
        "temperature": 0
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'sk-E9F0tlYZpD8Oo5zM2ofIR7bk6rIbkfmXvEc7qFe8pH1id9hS'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    #print(data)
    data = json.loads(data)
    choices = data["choices"]
    message = choices[0]['message']
    content = message['content']
    return content


def rank_v1(gpt_answer):
    # 使用非贪婪匹配提取 *** 与 *** 之间的内容
    pattern_star = r'\*\*\*(.*?)\*\*\*'
    match_star = re.search(pattern_star, gpt_answer, re.DOTALL)
    score = match_star.group(1).strip() if match_star else ""
    score = score.replace("[", "").replace("]", "").replace(" ", "")

    if '0' <= score <= '5':
        return float(score)
    else:
        # print(score)
        return 0



def write_answer(output_path, no, question, evidence):
    with open(output_path, 'a', encoding='utf-8') as f:
        f.write(json.dumps({"no": no, "question": question, "evidence": evidence}, ensure_ascii=False) + "\n")


def generate_evidence(i, question, add_path):
    try:
        while 1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(gpt_api, question, 'gpt-3.5-turbo')
                evidence = future.result(timeout=10)
            # evidence = gpt_api(question, 'gpt-3.5-turbo')
            #evidence = deepseek_api(question)
            write_answer(add_path, i + 1, question, evidence)
            print(f"{i + 1} finish")
            break
    except concurrent.futures.TimeoutError:
        print("gpt_api 超时，重试 ...")
    except (KeyError, TimeoutError, IndexError, json.decoder.JSONDecodeError, http.client.RemoteDisconnected, ssl.SSLEOFError):
        print("retrying ...")


def extract_evidence(file_path, i):
    #file_path = '35t-test_sum-complement.jsonl'
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = ast.literal_eval(line)
            no = line['no']
            if no == (i + 1):
                evidence = line['evidence']
                matches = re.findall(r'\*\*\*(.*?)\*\*\*', evidence)
                matches = [match.strip('{}') for match in matches]
                if matches:
                    return matches[0]
                else:
                    return ""


def main():
    com_path = 'score.jsonl'

    with open('mss-dpr-erank.json', 'r') as f:
        sum_data = json.load(f)

    a = 0
    with open(com_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < 2919:
                continue
            line = line.strip()
            line = ast.literal_eval(line)
            question = line['question']
            answer = line['answer']
            evidence = ""
            if answer:
                evidence_score = rank_v1(answer)
                if evidence_score != 0:

                    for j, e in enumerate(sum_data[i]["selected_evidences"]):
                        evidence = e
                        break

            if not evidence:
                a += 1

                # # 生成并保存证据
                generate_evidence(i, question, 'add_evidence.jsonl')

                # 调用生成结果
                # evidence = extract_evidence('gpt_result-A/add_evidence.jsonl', i)
                # print(evidence)
                # print(i+1)
    #         sum_data[i]['rerank_first'] = evidence
    #
    # with open('/mnt/Disk2/hengyu24/reano-modify/CEQA-main/dataset/NQ/MSS-DPR/gpt_evaluate-v1.json', 'w') as f:
    #     json.dump(sum_data, f, indent=4)

    print(a)

    print("finish")


if __name__ == '__main__':
    main()
