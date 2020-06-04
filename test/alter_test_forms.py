from quiz_card.cards.forms import CreateForm


class TestCreateForm:
    """Test Create Form"""

    def test_validate_success(self, db):
        form = CreateForm(question="question",
                          answer="answer",
                          link="link")
        assert form.validate() is True
