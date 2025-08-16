from medical.models import Answer

def create_attempt_with_answers(attempt):
    for question in attempt.questionnaire.questions.all():
        Answer.objects.create(
            question=question,
            attempt=attempt,
            answer=False,
            is_needed=False,
            is_covered=False,
            notes="",
        )
