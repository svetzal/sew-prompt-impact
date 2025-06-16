from mojentic.llm import LLMBroker, MessageBuilder

from assessor.output_processors.strip_thinking import strip_thinking


def generate_cross_model_assessments(llm: LLMBroker, output_files_collector):
    for source_file, outputs in output_files_collector.items():
        if not outputs:
            continue

        # Create assessment prompt
        assessment_prompt = f"""
        Please assess the quality and differences between the following outputs generated for the 
        source document '{source_file.name}'.
        In the assessment refer to each output by its filename.
        """

        mb = MessageBuilder(assessment_prompt)
        mb.add_file(source_file)
        mb.add_files(*outputs)

        assessment = llm.generate(messages=[mb.build()])

        # Strip out thinking text
        assessment = strip_thinking(assessment)

        assessment_file_path = source_file.with_name(
            f"{source_file.stem}-assessment{source_file.suffix}")
        with open(assessment_file_path, 'w') as assessment_file:
            assessment_file.write(assessment)

        print(f"Created assessment for {source_file.name} -> {assessment_file_path.name}")
