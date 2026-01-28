# Question: Develop a simple expert system using rule-based reasoning/fuzzy logic.

"""
MEDICAL EXPERT SYSTEM
Multiple diseases with explanation and visualization
"""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class CompleteMedicalExpert:
    """Comprehensive medical diagnosis system"""

    def __init__(self):
        self.diseases = self._load_disease_database()
        self.fuzzy_ctrls = self._setup_fuzzy_controls()
        self.patient_history = []

    def _load_disease_database(self):
        """Comprehensive disease knowledge base"""
        return {
            'Influenza': {
                'symptoms': ['fever', 'cough', 'fatigue', 'body_ache', 'headache'],
                'required': ['fever', 'cough'],
                'risk_factors': ['elderly', 'chronic_illness', 'pregnancy'],
                'treatments': ['Antiviral (Tamiflu)', 'Rest', 'Fluids', 'Pain relievers'],
                'urgency': 'medium'
            },
            'Common Cold': {
                'symptoms': ['runny_nose', 'sneezing', 'sore_throat', 'cough', 'mild_fever'],
                'required': ['runny_nose'],
                'risk_factors': [],
                'treatments': ['Rest', 'Antihistamines', 'Nasal decongestant'],
                'urgency': 'low'
            },
            'COVID-19': {
                'symptoms': ['fever', 'cough', 'shortness_of_breath', 'loss_of_taste',
                           'loss_of_smell', 'fatigue'],
                'required': ['fever', 'cough'],
                'risk_factors': ['elderly', 'diabetes', 'heart_disease', 'obesity'],
                'treatments': ['Isolation', 'Medical consultation', 'Symptomatic treatment'],
                'urgency': 'high'
            },
            'Pneumonia': {
                'symptoms': ['high_fever', 'cough_with_phlegm', 'chest_pain',
                           'shortness_of_breath', 'fatigue'],
                'required': ['high_fever', 'cough_with_phlegm'],
                'risk_factors': ['smoking', 'lung_disease', 'weak_immune'],
                'treatments': ['Antibiotics', 'Hospitalization', 'Oxygen therapy'],
                'urgency': 'high'
            }
        }

    def _setup_fuzzy_controls(self):
        """Setup multiple fuzzy controllers"""
        controllers = {}

        # Fever severity controller
        fever = ctrl.Antecedent(np.arange(35, 42, 0.1), 'fever')
        fever['normal'] = fuzz.trimf(fever.universe, [35, 36.5, 37.5])
        fever['mild'] = fuzz.trimf(fever.universe, [37, 37.8, 38.5])
        fever['high'] = fuzz.trimf(fever.universe, [38, 39.5, 42])

        severity = ctrl.Consequent(np.arange(0, 101, 1), 'severity')
        severity['low'] = fuzz.trimf(severity.universe, [0, 0, 40])
        severity['medium'] = fuzz.trimf(severity.universe, [30, 50, 70])
        severity['high'] = fuzz.trimf(severity.universe, [60, 100, 100])

        rules = [
            ctrl.Rule(fever['high'], severity['high']),
            ctrl.Rule(fever['mild'], severity['medium']),
            ctrl.Rule(fever['normal'], severity['low'])
        ]

        controllers['fever'] = ctrl.ControlSystemSimulation(ctrl.ControlSystem(rules))
        return controllers

    def interactive_diagnosis(self):
        """Interactive diagnosis session"""
        print("\n--------------------------------")
        print("COMPLETE MEDICAL EXPERT SYSTEM")
        

        # Collect symptoms
        symptoms = self._collect_symptoms()

        # Analyze
        results = self._analyze_symptoms(symptoms)

        # Generate report
        self._generate_report(results, symptoms)

        # Visualize if requested
        self._visualize_fuzzy_sets()

    def _collect_symptoms(self):
        """Interactive symptom collection"""
        symptoms = {}

        print("\nPlease answer the following questions (y/n):")

        questions = [
            ('fever', 'Do you have fever? If yes, enter temperature (e.g., 38.5): '),
            ('cough', 'Do you have cough? Rate severity 0-10: '),
            ('fatigue', 'Do you feel fatigued? '),
            ('runny_nose', 'Do you have runny nose? '),
            ('shortness_of_breath', 'Do you have shortness of breath? '),
            ('loss_of_taste', 'Have you lost sense of taste? '),
            ('body_ache', 'Do you have body aches? '),
            ('headache', 'Do you have headache? ')
        ]

        for symptom, question in questions:
            response = input(f"\n{question}").strip().lower()
            if response in ['y', 'yes', 'true']:
                symptoms[symptom] = True
            elif symptom == 'fever' and response.replace('.', '').isdigit():
                symptoms['fever'] = True
                symptoms['fever_temp'] = float(response)
            elif symptom == 'cough' and response.isdigit():
                symptoms['cough'] = True
                symptoms['cough_level'] = int(response)
            elif response in ['n', 'no', 'false']:
                symptoms[symptom] = False

        return symptoms

    def _analyze_symptoms(self, symptoms):
        """Analyze symptoms against disease database"""
        results = []

        for disease, data in self.diseases.items():
            score = 0
            matched_symptoms = []
            explanation = []

            # Check required symptoms
            has_required = all(symptom in symptoms and symptoms[symptom]
                             for symptom in data['required'])

            if not has_required:
                continue

            # Calculate matching score
            for symptom in data['symptoms']:
                if symptom in symptoms and symptoms[symptom]:
                    score += 1
                    matched_symptoms.append(symptom)
                    explanation.append(f"Has {symptom.replace('_', ' ')}")

            # Calculate percentage match
            match_percent = (score / len(data['symptoms'])) * 100

            # Assess urgency with fuzzy logic
            urgency_score = self._assess_urgency(symptoms, disease)

            results.append({
                'disease': disease,
                'match_percent': match_percent,
                'matched_symptoms': matched_symptoms,
                'explanation': explanation,
                'treatments': data['treatments'],
                'urgency': data['urgency'],
                'urgency_score': urgency_score
            })

        return sorted(results, key=lambda x: x['match_percent'], reverse=True)

    def _assess_urgency(self, symptoms, disease):
        """Fuzzy logic urgency assessment"""
        if 'fever_temp' in symptoms and disease in self.fuzzy_ctrls:
            ctrl = self.fuzzy_ctrls['fever']
            ctrl.input['fever'] = symptoms['fever_temp']
            ctrl.compute()
            return ctrl.output['severity']
        return 50  # Default medium

    def _generate_report(self, results, symptoms):
        """Generate comprehensive diagnosis report"""
        print("\n--------------------")
        print("DIAGNOSIS REPORT")
        

        if not results:
            print("\nNo matching diseases found.")
            print("Recommendation: Consult a doctor for accurate diagnosis.")
            return

        print(f"\nFound {len(results)} possible conditions:")

        for i, result in enumerate(results[:3], 1):  # Top 3
            print(f"\n{i}. {result['disease']}:")
            print(f"   Match: {result['match_percent']:.1f}%")
            print(f"   Urgency: {result['urgency']} ({result['urgency_score']:.1f}/100)")

            print(f"\n   Symptoms present:")
            for symptom in result['matched_symptoms'][:5]:  # Show top 5
                print(f"   ✓ {symptom.replace('_', ' ')}")

            print(f"\n   Recommended treatments:")
            for treatment in result['treatments']:
                print(f"   • {treatment}")

            print(f"\n   Reasoning: {'; '.join(result['explanation'][:3])}...")
            print("-"*40)

    def _visualize_fuzzy_sets(self):
        """Visualize fuzzy membership functions"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        # Fever membership visualization
        fever = np.arange(35, 42, 0.1)
        normal = fuzz.trimf(fever, [35, 36.5, 37.5])
        mild = fuzz.trimf(fever, [37, 37.8, 38.5])
        high = fuzz.trimf(fever, [38, 39.5, 42])

        axes[0].plot(fever, normal, 'b', linewidth=2, label='Normal')
        axes[0].plot(fever, mild, 'g', linewidth=2, label='Mild')
        axes[0].plot(fever, high, 'r', linewidth=2, label='High')
        axes[0].set_title('Fever Severity Membership Functions')
        axes[0].set_xlabel('Temperature (°C)')
        axes[0].set_ylabel('Membership')
        axes[0].legend()
        axes[0].grid(True)

        # Severity output visualization
        severity = np.arange(0, 101, 1)
        low = fuzz.trimf(severity, [0, 0, 40])
        medium = fuzz.trimf(severity, [30, 50, 70])
        high_sev = fuzz.trimf(severity, [60, 100, 100])

        axes[1].plot(severity, low, 'g', linewidth=2, label='Low')
        axes[1].plot(severity, medium, 'y', linewidth=2, label='Medium')
        axes[1].plot(severity, high_sev, 'r', linewidth=2, label='High')
        axes[1].set_title('Disease Severity Output')
        axes[1].set_xlabel('Severity Score')
        axes[1].set_ylabel('Membership')
        axes[1].legend()
        axes[1].grid(True)

        plt.tight_layout()
        plt.savefig('fuzzy_visualization.png', dpi=150)
        print("\n✓ Fuzzy sets visualization saved as 'fuzzy_visualization.png'")

# Example usage
def run_system_b():
    """Demo of Complete Medical System"""
    expert = CompleteMedicalExpert()
    expert.interactive_diagnosis()

if __name__ == "__main__":
    run_system_b()

