class SurveyDataAggregator:
    def __init__(self):
        self.data = {}

    def add_survey(self, survey_id, questions):
        if survey_id not in self.data:
            self.data[survey_id] = {}
        for question, answer in questions.items():
            if question not in self.data[survey_id]:
                self.data[survey_id][question] = []
            self.data[survey_id][question].append(answer)

    def get_survey_results(self, survey_id):
        if survey_id not in self.data:
            return {}
        return self.data[survey_id]

    def get_question_results(self, survey_id, question):
        if survey_id not in self.data:
            return []
        if question not in self.data[survey_id]:
            return []
        return self.data[survey_id][question]

    def get_average_answer(self, survey_id, question):
        results = self.get_question_results(survey_id, question)
        if not results:
            return None
        return sum(results) / len(results)

    def get_most_common_answer(self, survey_id, question):
        results = self.get_question_results(survey_id, question)
        if not results:
            return None
        return max(set(results), key=results.count)


# Misol
aggregator = SurveyDataAggregator()
aggregator.add_survey("1", {"Q1": "A", "Q2": "B"})
aggregator.add_survey("1", {"Q1": "A", "Q2": "C"})
aggregator.add_survey("2", {"Q1": "B", "Q2": "A"})

print(aggregator.get_survey_results("1"))  # {"Q1": ["A", "A"], "Q2": ["B", "C"]}
print(aggregator.get_question_results("1", "Q1"))  # ["A", "A"]
print(aggregator.get_average_answer("1", "Q1"))  # 0.5
print(aggregator.get_most_common_answer("1", "Q1"))  # "A"
