from time import sleep
import openai
import os
import os.path as osp
import config as cfg
import json
import argparse

# openai.api_key = "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"
openai.api_key = cfg.OPENAI_APIKEY


def ie_gpt(args):
    # filename = osp.basename(file)
    text = ''.join(c for c in open(args.request_path, "r", encoding='utf-8').readlines())

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": f"{text}"}
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    with open(args.output_path, "w", encoding='utf-8') as oup_obj:
        oup_obj.write(result)
    sleep(10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--request_path', type=str, default='request.txt', help='Path to the request saved in txt format')
    parser.add_argument('--output_path', type=str, default='output.txt')
    
    args = parser.parse_args()
    
    ie_gpt(args)