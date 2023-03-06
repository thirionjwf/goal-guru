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
                "content": f"""
                    You are an employee, working as a {title} in an insurance company.
                    You're manager has given you the following high-level objective which you need to use to create a SMART goal for 2023:
                    {objective}
                    You need to write SMART goals broken up in clear and specific goals, an approach to measure the outcome (and in addition suggest a scale of 1-5 for measurement.
                    The principle of the measurement scale is that a 1 indicates under-performing significantly, 2 sometimes under-performing, 3 is achieving what has been asked, 4 is significantly outperforming, and 5 indicates that the individual redefined what a score of 3 should be.
                    The measurement scale needs to be adapted and made relevant to the specific SMART goal.
                    """,
            },
            {
                "role": "user",
                "content": "Return the SMART goals, measurement approach, measurement scale, target date, and possible milestones with all these fields separated with newlines.",
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
