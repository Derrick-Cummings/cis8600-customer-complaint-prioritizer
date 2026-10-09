# Evaluation Results

## Test approach

The NovaMart Customer Complaint Prioritizer was tested using fictional customer complaints representing different urgency levels and customer-service scenarios.

Testing focused on whether the application could:

Classify complaints as High, Medium, or Low urgency.

Identify customer sentiment.

Generate professional draft responses for human review.

Return results successfully through the AWS-hosted web interface.

The urgency classifications were reviewed against the definitions established in the system prompt. Testing was exploratory and did not constitute a formal quantitative model evaluation.

## Results

The completed prototype successfully processed fictional customer complaints and returned urgency classifications, sentiment assessments, and draft responses.

Testing identified some inconsistencies in urgency classification, particularly when distinguishing between complaints involving genuine risk and complaints expressing strong dissatisfaction.

Prompt refinements improved the clarity of the classification instructions.

No formal accuracy, precision, recall, or other quantitative performance metrics were calculated.

## Changes made

The following refinements were made during development:

Added clearer definitions for High, Medium, and Low urgency.

Included representative complaint examples for each urgency category.

Clarified that angry language alone does not justify a High urgency classification.

Instructed the model not to claim that refunds, replacements, or escalations had already occurred.

Retested the application using fictional complaints after prompt adjustments.

## Changes made

Testing was conducted using fictional complaints rather than actual customer records.

The project did not include a labeled production evaluation dataset, a formal model benchmark, or measured improvements in customer-service response times.

Further evaluation would be necessary before deploying the application in a real customer-service environment.
