import os
import openai
from api import api_key

openai.api_key = api_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my mom wishing her a happy birthday\n\nSubject line: Wishing you a Happy Birthday, Mom!\n\nHi Mom, \n\nI wanted to take a quick moment out of your special day to wish you a very, very Happy Birthday! I hope it's filled with lots of love, happiness, and joy. You deserve to have an unforgettable day! \n\nI miss you so much and wish I could be there with you to celebrate today. Instead, I hope you know that I'm thinking about you from a distance and sending lots of birthday hugs and kisses your way. \n\nI love you so much and cannot believe how quickly time has flown! You're the most amazing mom I could ever ask for, and I'm so thankful to have you in my life. \n\nHave a wonderful day!\n\nLove, \nYour daughter",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)


'''
{
  "id": "cmpl-7d10j8ejwnOWRJKdV4oXtC3iUa04N",
  "object": "text_completion",
  "created": 1689533033,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 181,
    "total_tokens": 181
  }
}
'''
