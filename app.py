import config
import gradio as gr
import openai
import pandas as pd


def get_goal(title: str, objective: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f'''
                    You are an employee, working as a {title} in an insurance company. The insurance company sells short-term, on-demand, single item and car insurance.

                    You need to write SMART goals to be used for your yearly performance evaluation. The SMART goals need to be broken up in clear and specific goals, an approach to measure the outcome, and in addition suggest a scale of 1-5 for measurement.

                    The following CSV table shows the measurement scale proposed for developing measurement criteria. These need to be customised for each specific goal:
                    Legend,Short Description,Scale,Name,Goals,Values;
                    "1,Performance significantly below par,>75%,Non-performer,""Most of the goals have not been achieved to the agreed standard";
                    • Not performing the essentials of the job;
                    • Poor performance despite developmental / coaching interventions;
                    • Below target / performance on most occasions;
                    " • Constant supervision and follow-up required"",""Seldom Demonstrated";
                    " • Does not consistently act in line with our Values. Behaviours have not reflected the high standards expected in a number of situations.""";
                    "2,Performance below par,75%+,Developing performer - approaching competence,""Achieved Most:+75% of goals have been achieved ";
                    • Still learning the essentials of the role and improving towards effective performance;
                    • Met target or completed goals on most occasions, however not in all;
                    • Requires some supervision and follow-up;
                    " • Has good skills and capabilities, however still needs further development and coaching"",""Mostly Demonstrated";
                    " • Acts in line with our values, consistently demonstrating the behaviours associated with each value across different situations.""";
                    "3,Performance on par,100%,Solid Performer - sufficiently competent,""Solid Performer - sufficiently competent";
                    • Performs all functions effectively;
                    • Consistently met all targets and goals and sometimes exceeded targets;
                    • Looks to enhance own performance and that of others. Made a contribution beyond own job to team/BU/organisation;
                    • Rarely needed supervision or follow-up;
                    " • Demonstrates sound capabilities, however still has room for development of specific skills"",""Always Demonstrated";
                    • Lives our values in a proactive way, clearly demonstrating;
                    to others how they guide everyday actions and decisions;" consistently demonstrates the behaviours associated with each value, even in challenging situations"""
                    "4,Performance exceeding par consistently,100%+,Exceeds Expectations,""Excelling Performer - exceeds required competence";
                    • Contributes more than effective performance and effects measurable and lasting improvements in team/BU/organisation performance;
                    • Changed the way the team/BU/organisation operates and provided great value to customer experience and/or profitability;
                    • Far exceeded targets and goals in all areas;
                    • Consistently takes the best approach to get the job done and anticipates challenges;
                    " • Acts as a role model for others"",""Exceeds Expectations";
                    " • Acts and is considered to be an inspirational role model for all our values, clearly demonstrating to others how they guide everyday actions and decisions, particularly in high stakes or difficult/ pressure situations. Actively supports and challenges the behaviours of colleagues in order that they might do the same.""";
                    "5,Performance at level that requires revisiting of par,110%,Walking on water,""Super Star - exceeds all competence";
                    • Contributes more than effective performance and effects measurable and lasting improvements in team/BU/organisation performance;
                    • Changed the way the team/BU/organisation operates and provided great value to customer experience and/or profitability;
                    • Far exceeded targets and goals in all areas;
                    • Consistently takes the best approach to get the job done and anticipates challenges;
                    • Acts as a role model for others;
                    " • Develops and deploys game changing innovations"",""Exceeds Expectations";
                    " • Acts and is considered to be an inspirational role model for all our values, clearly demonstrating to others how they guide everyday actions and decisions, particularly in high stakes or difficult/ pressure situations. Actively supports and challenges the behaviours of colleagues in order that they might do the same. Mentors others to achieve exceptional results.""";

                    Here is an example input objective from your manager:

                    1. You need to achieve a delivery objective where you will get a team score from the Agile Sprint burn rate for the team. A good aim for a burn rate in the 2-week Sprint is 80-85%. The measure will be the average over all Sprints for the year.

                    I need you to return for each high-level input objective, an output that looks like the following:
                    GOAL:
                    Achieve an 80% burn rate on average over all Sprints, by Q4, to improve our ability to deliver projects on-time.
                    MEASUREMENT:
                    Use the JIRA burn down report to calculate the burn rate and calculate the average burn rate for the year.
                    1. Burn rate is <50%
                    1. Burn rate is 50-75%
                    3. Burn rate is 75-85%
                    4. Burn rate is 85%-100%
                    5. Burn rate is >100%
                    TARGET
                    2023 Q4
                    MILESTONES
                    Q1: Average burn rate is to be measured and a baseline established
                    Q2: Average burn rate is over 75%
                    Q3: Average burn rate is over 80%
                    Q4: Average burn rate of 80% achieved

                    You're manager has given you the following high-level objectives which you need to use to create a SMART goal for 2023:
                    {objective}

                    Return the SMART goals, measurement approach, measurement scale, target date, and possible milestones with all these goals separated with newlines, as in the example output given above for each high-level objective listed.
                ''',
            },
        ],
    )

    return response.choices[0]["message"]["content"]


def get_interface():
    with gr.Blocks() as iface:
        job_desc = gr.Textbox(placeholder="Your job title", label="Job description")
        objective = gr.Textbox(
            lines=15,
            placeholder="Enter high-level objectives here, one per line, e.g.:\n1. Increase sales of new contracts by 10%, to boost the revenue of the company.\n2. Retain high-value customers by reducing churn by 25%.",
            label="Objective",
        )
        output_goal = gr.Textbox(label="Goal")

        get_btn = gr.Button("Get my goals")
        get_btn.click(
            fn=get_goal,
            inputs=[job_desc, objective],
            outputs=output_goal,
        )

    return iface


def main():
    cfg = config.Config(".env")
    openai.api_key = cfg["OPEN_AI_API_KEY"]

    company_objectives = pd.read_csv("company_objectives.csv")
    print(company_objectives.info())

    get_interface().launch(share=False)
    return


main()
