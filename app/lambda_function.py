# This file will contain the AWS Lambda function for the Customer Complaint Prioritizer.
# It will receive a fictional complaint, call Amazon Bedrock, and return the analysis.

import json 

import boto3 

from botocore.exceptions import ClientError 

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1") 

MODEL_ID = "us.anthropic.claude-haiku-4-5-20251001-v1:0" 

SYSTEM_PROMPT = """ 

You are a customer complaint prioritizer. 

Read the customer complaint and return only valid JSON with: 
- urgency: High, Medium, or Low 
- sentiment: Angry, Frustrated, or Neutral 
- draft_response: a short, professional response for a customer-service agent to review 
Classify urgency using these definitions: 

  
High: Use only when the complaint involves immediate safety, health, food-safety, account-security, fraud or unauthorized access, a duplicate charge creating an immediate financial problem, a recurring / persistent issue, or another issue requiring urgent human review. For example:
    Safety hazard: The space heater I bought yesterday started smoking after 20 minutes of use. I unplugged it immediately because I am worried it could cause a fire
    Health concern: My daughter ate one of the snack bars I purchased and started having an allergic reaction. The package did not clearly list the ingredient we believe caused it.
    Food safety: I picked up a grocery order this afternoon, and the milk and chicken were warm when I got home. I do not feel safe using them.
    Account security: I received an order confirmation for an order I never placed. When I checked my account, my delivery address had been changed.
    Fraud/unauthorized access: There are purchases on my account that I did not make. I believe someone has used my account without permission.
    Duplicate charge: I was charged twice for the same order, and the duplicate charge has affected the money available in my bank account.
    Persistent serious issue: I have contacted support three times because the charging cable I received repeatedly becomes extremely hot while charging my device. The issue has still not been resolved.
Medium: Use when the problem has a meaningful customer impact but does not involve immediate safety, security, or serious financial risk. Examples include a damaged unusable product, request for refund, or late paid-expedited delivery. For Example:
    Damaged, non-dangerous product: The television I purchased arrived with a cracked screen. It cannot be used, and I would like to know my replacement or refund options.
    Delayed refund: I returned shoes two weeks ago, and tracking shows the return was received eight days ago. I still have not received my refund.
    Late expedited delivery: I paid extra for two-day shipping because I needed the item for a birthday. It arrived four days late, after the birthday had passed.
    Missing item: My order arrived today, but one of the items listed on the packing slip was not in the box. Can someone help me get the missing item?
    Repeated unresolved issue without harm: contacted customer service twice last week because my account will not let me update my delivery address. The problem is still not fixed.
Low: Use for routine questions, minor inconvenience, standard return or exchange requests, product-availability questions, or ordinary shipping-status requests. For Example:
    Return instructions: Could you please send me the return instructions for an item I purchased last week?
    Exchange request: I received a blue comforter, but I ordered gray. How can I exchange it?
    Product availability: Will the NovaMart winter-coat collection be available online this month?
    Shipping-status request: I placed an order three days ago, and the tracking still says ‘label created.’ Could you tell me the expected delivery window? 
    Routine question: Can I cancel my order if it has not shipped yet?

  
Do not classify a complaint as High only because the customer uses angry language or asks for immediate help. Classify based on the actual risk and impact. 
Do not claim that a refund, escalation, replacement, or other action has already happened. The draft response should state that the issue will be reviewed. 
Return only valid JSON. 

""" 
 

def lambda_handler(event, context): 

    try: 

        # Works for a direct Lambda test and later for API Gateway. 

        if event.get("body"): 

            body = event["body"] 

  

            if isinstance(body, str): 

                payload = json.loads(body) 

            else: 

                payload = body 

        else: 

            payload = event 

  

        complaint = payload.get("complaint", "").strip() 

  

        if not complaint: 

            return { 

                "statusCode": 400, 

                "headers": { 

                    "Content-Type": "application/json" 

                }, 

                "body": json.dumps({ 

                    "error": "A complaint is required." 

                }) 

            } 

  

        response = bedrock.converse( 

            modelId=MODEL_ID, 

            system=[ 

                { 

                    "text": SYSTEM_PROMPT 

                } 

            ], 

            messages=[ 

                { 

                    "role": "user", 

                    "content": [ 

                        { 

                            "text": complaint 

                        } 

                    ] 

                } 

            ], 

            inferenceConfig={ 

                "maxTokens": 500, 

                "temperature": 0.2 

            } 

        ) 

  

        result = response["output"]["message"]["content"][0]["text"] 

  

        return { 

            "statusCode": 200, 

            "headers": { 

                "Content-Type": "application/json" 

            }, 

            "body": json.dumps({ 

                "analysis": result 

            }) 

        } 

  

    except json.JSONDecodeError: 

        return { 

            "statusCode": 400, 

            "headers": { 

                "Content-Type": "application/json" 

            }, 

            "body": json.dumps({ 

                "error": "The request body must contain valid JSON." 

            }) 

        } 

  

    except ClientError as error: 
        print(f"Bedrock error: {error}")

        return { 

            "statusCode": 500, 

            "headers": { 

                "Content-Type": "application/json" 

            }, 

            "body": json.dumps({ 

                "error": "An internal error occurred while processing the complaint." 

            }) 

        } 
