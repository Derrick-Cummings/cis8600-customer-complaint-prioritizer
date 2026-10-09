# NovaMart Customer Complaint Prioritizer
### A Generative AI Proof of Concept

## Project Overview

The NovaMart Customer Complaint Prioritizer is a generative AI application developed to help customer-service agents identify urgent complaints, assess customer sentiment, and prepare response drafts for human review.

The project was developed as a team-based proof of concept for NovaMart, a fictional e-commerce retailer. It demonstrates how generative AI and AWS serverless services can support customer-service operations and digital transformation.

## Business Problem

NovaMart processes approximately 800–1,200 customer complaints daily using a largely manual, first-come, first-served process.

Key challenges include:

- No systematic method for prioritizing urgent complaints.
- An average complaint response time of 18 hours.
- Delayed responses that can negatively affect customer satisfaction and retention.

The business objective is to improve complaint prioritization and support NovaMart's strategic goal of reducing average response time to four hours.

**Note:** The four-hour target is a proposed business goal, not a measured result of this prototype.

## Solution Overview

The application allows a customer-service agent to submit a fictional customer complaint and receive:

- **Urgency classification:** High, Medium, or Low.
- **Sentiment assessment:** AI-generated analysis of customer sentiment.
- **Draft response:** A suggested customer-service response requiring human review.

Agents can accept, modify, or copy the draft. The application does not automatically send responses to customers.

## Technology Stack

| Component | Technology |
|---|---|
| Large language model | Anthropic Claude Haiku 4.5 |
| Model access | Amazon Bedrock |
| Backend processing | AWS Lambda (Python) |
| API integration | Amazon API Gateway |
| Frontend | HTML, CSS, JavaScript |
| Web hosting | Amazon S3 |
| Operational monitoring | Amazon CloudWatch |

## How the Application Works

1. An agent enters a fictional customer complaint in the web interface.
2. The webpage sends the complaint to Amazon API Gateway.
3. AWS Lambda processes the request and invokes Claude Haiku 4.5 through Amazon Bedrock.
4. The model generates an urgency classification, sentiment assessment, and response draft.
5. The results are displayed in the web interface for agent review.

## Implementation and Testing

A functioning end-to-end proof of concept was deployed using AWS serverless services.

Testing with fictional customer complaints helped identify and address challenges involving urgency-classification consistency, AWS region availability, API connectivity, CORS configuration, and integration between application components.

The project demonstrated technical functionality but did not measure actual reductions in complaint response times, customer satisfaction improvements, or other production business outcomes.

## Future Enhancements

The project report discusses several potential production capabilities:

- Supervised fine-tuning using verified complaint and response data.
- Reinforcement learning from human feedback.
- A production feedback loop for monitoring response quality and incorporating employee feedback.
- A controlled agentic workflow capable of performing authorized customer-service actions through enterprise-system integrations.

These capabilities were explored conceptually and were **not implemented in the current prototype**.

## Project Documentation

[Read the Full Project Report](docs/NovaMart_Customer_Complaint_Prioritizer.pdf)

## Repository Structure

```text
app/
├── frontend/
│   └── index.html
├── lambda_function.py
└── prompt.py

docs/
├── NovaMart_Customer_Complaint_Prioritizer.pdf
└── evaluation_results.md

tests/

README.md
requirements.txt
.gitignore
```

## Running the Application

The frontend source code is available in `app/frontend/index.html`.

To connect the interface to a deployed backend, replace the placeholder API Gateway URL with the appropriate endpoint. Running the full application requires AWS infrastructure, access to Amazon Bedrock, and correctly configured API Gateway and Lambda services.

The repository does not include AWS credentials. Only fictional customer complaints should be used for demonstration purposes.

## Project Contributions

This application was developed as a collaborative team project.

**My contributions:** My Role — Project Lead: Led the NovaMart Customer Complaint Prioritizer project from business case development and project planning through solution implementation. Directed the overall project approach, actively contributed to building and implementing the generative AI application, and served as the primary author of the project report.

**Team contributions:** Collaborated with team members throughout the project's development and implementation. Chris also authored the Agentic AI section of the project report.

## Project Status

**Completed:** Deployed proof-of-concept application.

**Not implemented:** Production customer-service integrations, automated customer responses, fine-tuning, reinforcement learning from human feedback, and agentic workflows.
