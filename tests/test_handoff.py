import unittest
from docassemble.HarborIntakeDemo.handoff import build_payload, simulate_handoff


class HandoffTests(unittest.TestCase):
    def payload(self, **overrides):
        args = dict(first='Jordan', last='Rivera', email='jordan@example.com', phone='555-0100', contact_method='Email', safe_contact='No voicemail', language='Spanish', problem='Housing', details='Repair dispute', housing_issue='Repairs', deadline='2026-11-05', household_size=3, monthly_income=2450, documents=[{'filename':'fictional.txt'}])
        args.update(overrides)
        return build_payload(**args)

    def test_actual_answers_and_attachment_metadata(self):
        p = self.payload()
        self.assertEqual(p['client']['first_name'], 'Jordan')
        self.assertEqual(p['household'], {'size':3, 'monthly_income':2450.0})
        self.assertEqual(p['documents'][0]['filename'], 'fictional.txt')
        self.assertEqual(p['matter']['priority'], 'Deadline review')

    def test_obsolete_branch_answers_are_excluded(self):
        p = self.payload(problem='Family', contact_method='Do not contact me', deadline=None)
        self.assertIsNone(p['matter']['housing_issue'])
        self.assertIsNone(p['client']['email'])
        self.assertIsNone(p['client']['phone'])
        self.assertEqual(p['matter']['priority'], 'Standard review')

    def test_phone_preference_excludes_old_email(self):
        p = self.payload(contact_method='Phone')
        self.assertEqual(p['client']['phone'], '555-0100')
        self.assertIsNone(p['client']['email'])

    def test_consent_is_required(self):
        with self.assertRaises(ValueError):
            simulate_handoff(self.payload(), False)

    def test_repeat_submission_has_same_reference(self):
        a = simulate_handoff(self.payload(), True)
        b = simulate_handoff(self.payload(), True)
        self.assertEqual(a, b)
        self.assertTrue(a['simulation'])
        self.assertEqual(a['network_requests'], 0)
        self.assertNotEqual(a['reference'], simulate_handoff(self.payload(first='Alex'), True)['reference'])


if __name__ == '__main__':
    unittest.main()
