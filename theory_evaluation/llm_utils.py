import os
import re
import yaml


def initialise_prompt(agent: str):
    try:
        config_path = "./theory_evaluation/evaluator/prompts"
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        with open(f"{config_path}/{agent}/config.yaml") as file:
            config_values = yaml.load(file, Loader=yaml.loader.BaseLoader)

        with open(f"{config_path}/{agent}/prompt.txt", "r") as file:
            prompt_structure = file.read()

        # Define the placeholder pattern
        pattern = r"\{\$(\w+)\}"
        # Replace the placeholders in the prompt structure with the config_values
        for match in re.finditer(pattern, prompt_structure):
            placeholder = match.group(1)
            if placeholder in config_values:
                prompt_structure = re.sub(
                    r"\{\$" + placeholder + "\}",
                    config_values[placeholder],
                    prompt_structure,
                )
        return prompt_structure

    except Exception as e:
        print(f"{str(e)}: No configuration path to the prompt given.")


def initialise_settings(agent: str):
    try:
        config_path = "./theory_evaluation/evaluator/prompts"
        if not config_path:
            raise ValueError("CONFIG_PATH environment variable is not set")

        with open(f"{config_path}/{agent}/llm_settings.yaml") as file:
            return yaml.safe_load(file)

    except Exception as e:
        print(f"{str(e)}: No configuration path to the llm settings given.")


if __name__ == "__main__":
    # initialise_prompt(agent="short_discussion")
    initialise_settings("refactor_code")
