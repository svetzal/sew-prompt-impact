from assessor.output_processors.strip_thinking import strip_thinking


class DescribeStripThinking:

    def should_remove_thinking_tags_and_content(self):
        result = strip_thinking("<think>Thinking is here.</think> Answer is here.")

        assert result == "Answer is here."

    def should_handle_multiline_thinking_content(self):
        result = strip_thinking("""<think>
        multiline
        thinking
        part
        </think> 
        test.""")

        assert result == "test."
