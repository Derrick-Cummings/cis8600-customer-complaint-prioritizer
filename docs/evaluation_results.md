# Evaluation Results

## Test Approach

The NovaMart Customer Complaint Prioritizer was evaluated using five fictional customer complaints submitted through the deployed web interface.

The evaluation focused on whether the application could:

- Classify complaints as High, Medium, or Low urgency.
- Generate customer sentiment assessments.
- Produce draft responses for human review.
- Return results successfully through the AWS-hosted web interface.

Expected urgency classifications were determined using the definitions established in the system prompt and compared with the AI-generated classifications.

This was a small exploratory evaluation, not a formal production-level model assessment.

## Results

The following table summarizes the urgency-classification results from five fictional customer complaints.

| Test ID | Expected Urgency | Actual Urgency | Result |
|---|---|---|---|
| TC-01 | Low | Low | Pass |
| TC-02 | Medium | Medium | Pass |
| TC-03 | Medium | Medium | Pass |
| TC-04 | High | High | Pass |
| TC-05 | High | High | Pass |

A test was marked **Pass** when the actual urgency classification matched the expected classification.

## Evaluation Summary

All five AI-generated urgency classifications matched their expected classifications, resulting in **100% agreement (5/5)** on the selected fictional test cases.

The evaluation included:

- 1 Low-urgency complaint.
- 2 Medium-urgency complaints.
- 2 High-urgency complaints.

The application also successfully returned sentiment assessments and draft responses through the web interface.

These results demonstrate successful urgency classification for the five selected complaints but do not establish overall model accuracy or production reliability.

## Changes Made

During the initial development and testing process, the system prompt was refined to address inconsistencies in urgency classification.

The refinements included:

- Adding clearer definitions for High, Medium, and Low urgency.
- Providing representative complaint examples for each urgency category.
- Clarifying that angry language alone does not justify a High urgency classification.
- Instructing the model not to claim that refunds, replacements, or escalations had already occurred.
- Retesting the application with fictional complaints after prompt adjustments.

These changes were made during prototype development, before the five-test evaluation documented above.

## Evaluation Limitations

The evaluation used only five fictional customer complaints. Although all five urgency classifications matched their expected labels, the small test set does not establish overall model accuracy or production reliability.

The evaluation did not use real customer records or a comprehensive labeled dataset.

Sentiment accuracy and draft-response quality were not formally evaluated. The project also did not measure improvements in actual customer-service response times, customer satisfaction, or other business outcomes.

Further testing with a larger and more varied dataset would be necessary before considering production deployment.
