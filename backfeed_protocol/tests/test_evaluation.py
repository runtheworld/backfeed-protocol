from datetime import datetime
from ..contracts.dmag import DMagContract

from test_contract_base import BaseContractTestCase


class EvaluationTest(BaseContractTestCase):
    """test dmag protocol"""
    contract_class_to_test = DMagContract

    def test_get_evaluation(self):
        user = self.contract.create_user()
        contribution = self.contract.create_contribution(user=user)
        value = 1
        evaluation = self.contract.create_evaluation(contribution=contribution, user=user, value=value)

        evaluation = self.contract.get_evaluation(evaluation.id)

        self.assertEqual(evaluation.id, evaluation.id)
        self.assertEqual(evaluation.user, user)
        self.assertEqual(evaluation.contribution, contribution)
        self.assertEqual(evaluation.value, value)
        self.assertTrue(isinstance(evaluation.time, datetime))

    def test_get_evaluations(self):
        contract = self.get_contract_with_data()

        self.assertEqual(len(contract.get_evaluations(value=1)), 4)
        self.assertEqual(len(contract.get_evaluations(value=0)), 1)
        self.assertEqual(len(contract.get_evaluations(value=0)), 1)
        self.assertEqual(len(contract.get_evaluations(contribution_id=self.contribution0.id)), 3)
        self.assertEqual(len(contract.get_evaluations(contribution_id=self.contribution1.id)), 2)
        self.assertEqual(len(contract.get_evaluations(contribution_id=self.contribution2.id)), 0)
        self.assertEqual(len(contract.get_evaluations(evaluator_id=self.user0.id)), 0)
        self.assertEqual(len(contract.get_evaluations(evaluator_id=self.user1.id)), 1)
        self.assertEqual(len(contract.get_evaluations(evaluator_id=self.user2.id)), 2)
        self.assertEqual(len(contract.get_evaluations(evaluator_id=self.user3.id)), 2)