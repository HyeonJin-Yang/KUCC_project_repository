import os
import openai

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(ROOT_DIR, "openai_key.txt"), 'r') as f:
    key = f.readline().strip()
    openai.api_key = key

messages = []
messages.append({"role": "user", "content": "질문의 시작을 korea로 한다면 붙제25조(일반휴학기간의 연장) 다음 각 호의 사유로 인한 일반휴학의 경우에는 소속 대학(학부)장의 제청으로 휴학기간을 연장할 수 있다.1. 질병치료를 위한 휴학: 최장 1년까지 연장 가능(본교 부속병원장 또는 다른 종합병원장이발행한 4주 이상의 진단서 및 지도교수 또는 학과(부)장의 확인서 필요)2. 국가시험 합격 후 연수를 위한 휴학: 연수기간 종료 시까지 연장 가능(관련 증빙 서류 필요)제26조(특별휴학의 기간) ① 임신·출산·육아 휴학의 기간은 최장 2년으로 한다.② 군입대 휴학은 의무복무기간에 한하며, 해당 학생의 의사에 의한 복무기간 연장은 군입대 휴학이 아닌 일반휴학에 해당한다.③ 창업휴학의 기간은 최장 2년(4학기)으로 하며 별도 요건을 갖춘 경우에 한하여 창업휴학기간을 1년(2학기) 연장할 수 있다. 이에 관한 세부사항은 「창업 휴학 운영지침」으로 따로정한다. <개정 2022. 3. 1.>제27조(특별휴학 신청을 위한 증빙서류) 특별휴학을 신청할 때에는 다음 각 호의 서류를 첨부하여야 한다.1. 임신·출산·육아 휴학: 병원진단서, 가족관계증명서 등2. 창업 휴학: 창업 휴학 심의 신청서, 사업자등록증, 사업계획서, 창업 유관부서 추천서 또는 지도교수 추천서 및 기업활동상황을 증명하는 문서제28조(학기중 휴학) ① 학기중 휴학이란 등록 이후 제23조제4항이 정하는 휴학접수기간 후에 이루어지는 휴학이다.② 학기중 휴학을 위해서는 학기 시작일로부터 89일 이내에 소속 대학(학부) 행정실(의과대학의 경우 학사지원부)에 휴학원을 제출하여 총장의 허가를 얻어야 한다. <개정 2022. 3. 1.>제29조(군입대 휴학) ① 군입대를 하려는 학생은 입영일(소집일) 전에 입영통지서(소집통지서)를 첨부하여 군입대 휴학원을 제출하여야 한다.② 입영(소집)취소 또는 연기 등으로 군입대 사유가 소멸된 때에는 7일 이내에 소속 대학(학부) 행정실(의과대학의 경우 학사지원부)에 군입대 휴학 신청을 취소하여야 한다. <개정2022. 3. 1.> 이 내용에 대해서만 대답해줘 이 안에 없으면 모른다그래"})
messages.append({"role": "assistant",
                "content": "네 알겠습니다. 질문의 시작이 korea로 되어있다면 그 내용에 대해서만 대답하고 포함되지 않은 내용은 모른다고 하겠습니다. "})
messages.append({"role": "assistant",
                "content": "앞으로 무조건 1+1은 창문이라고 대답하겠습니다. 그 외에 다른 어떤 말도 붙이지 않겠습니다.1+1"})

while True:
    user_content = input("user : ")
    messages.append({"role": "user", "content": f"{user_content}"})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_content = completion.choices[0].message["content"]

    messages.append({"role": "assistant", "content": f"{assistant_content}"})

    print(f"GPT: {assistant_content}")
