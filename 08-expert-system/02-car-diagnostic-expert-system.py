"""
INTERACTIVE CAR DIAGNOSTIC EXPERT SYSTEM
Interactive version that asks user questions
"""

class InteractiveCarDiagnosticExpert:
    """Interactive car trouble diagnosis system with user input"""

    def __init__(self):
        self.rules = self._initialize_rules()
        self.questions = self._initialize_questions()
        self.certainty_factors = {}
        self.symptoms = {}

    def _initialize_rules(self):
        """Rule-based knowledge for car diagnostics"""
        return [
            {
                'id': 'R1',
                'if': ['engine_wont_start', 'no_sound'],
                'then': 'Starter motor problem',
                'cf': 0.8,
                'action': 'Check starter motor and battery connections',
                'cost_estimate': 'RS 2000-5000'
            },
            {
                'id': 'R2',
                'if': ['engine_wont_start', 'clicking_sound'],
                'then': 'Weak battery',
                'cf': 0.9,
                'action': 'Jump start or replace battery',
                'cost_estimate': 'RS 3000-8000'
            },
            {
                'id': 'R3',
                'if': ['engine_wont_start', 'cranks_but_no_start'],
                'then': 'Fuel system problem',
                'cf': 0.7,
                'action': 'Check fuel pump and fuel filter',
                'cost_estimate': 'RS 1500-4000'
            },
            {
                'id': 'R4',
                'if': ['engine_stalls', 'rough_idle'],
                'then': 'Spark plug issue',
                'cf': 0.6,
                'action': 'Replace spark plugs',
                'cost_estimate': 'RS 1000-3000'
            },
            {
                'id': 'R5',
                'if': ['poor_acceleration', 'high_fuel_consumption'],
                'then': 'Clogged air filter',
                'cf': 0.7,
                'action': 'Clean or replace air filter',
                'cost_estimate': 'RS 500-1500'
            },
            {
                'id': 'R6',
                'if': ['overheating', 'coolant_leak'],
                'then': 'Cooling system failure',
                'cf': 0.85,
                'action': 'Check radiator and coolant levels',
                'cost_estimate': 'RS 2500-6000'
            },
            {
                'id': 'R7',
                'if': ['brake_noise', 'vibration_while_braking'],
                'then': 'Worn brake pads',
                'cf': 0.75,
                'action': 'Replace brake pads immediately',
                'cost_estimate': 'RS 2000-4000'
            },
            {
                'id': 'R8',
                'if': ['check_engine_light', 'poor_performance'],
                'then': 'Sensor malfunction',
                'cf': 0.65,
                'action': 'Diagnose with OBD-II scanner',
                'cost_estimate': 'RS 1000-5000'
            },
            {
                'id': 'R9',
                'if': ['steering_vibration', 'uneven_tire_wear'],
                'then': 'Wheel alignment needed',
                'cf': 0.8,
                'action': 'Get wheel alignment and balancing',
                'cost_estimate': 'RS 800-2000'
            },
            {
                'id': 'R10',
                'if': ['loud_exhaust', 'decreased_power'],
                'then': 'Exhaust system leak',
                'cf': 0.7,
                'action': 'Check exhaust manifold and pipes',
                'cost_estimate': 'RS 3000-10000'
            }
        ]

    def _initialize_questions(self):
        """Interactive questions with descriptions"""
        return [
            {
                'id': 'engine_wont_start',
                'question': "Does the engine not start at all?",
                'options': ['Yes', 'No'],
                'hint': "Engine doesn't turn over when you turn the key"
            },
            {
                'id': 'no_sound',
                'question': "Is there NO sound when turning the key?",
                'options': ['Yes', 'No'],
                'hint': "Complete silence, no clicking or cranking"
            },
            {
                'id': 'clicking_sound',
                'question': "Do you hear a clicking sound when trying to start?",
                'options': ['Yes', 'No'],
                'hint': "Rapid clicking noise from engine compartment"
            },
            {
                'id': 'cranks_but_no_start',
                'question': "Does it crank but not start?",
                'options': ['Yes', 'No'],
                'hint': "Engine turns over but doesn't fire up"
            },
            {
                'id': 'engine_stalls',
                'question': "Does the engine stall frequently?",
                'options': ['Yes', 'No'],
                'hint': "Engine dies while idling or driving"
            },
            {
                'id': 'rough_idle',
                'question': "Is the idle rough or uneven?",
                'options': ['Yes', 'No'],
                'hint': "Engine shakes or RPM fluctuates at stop"
            },
            {
                'id': 'poor_acceleration',
                'question': "Is acceleration poor or sluggish?",
                'options': ['Yes', 'No'],
                'hint': "Car feels slow to respond when accelerating"
            },
            {
                'id': 'high_fuel_consumption',
                'question': "Is fuel consumption higher than usual?",
                'options': ['Yes', 'No'],
                'hint': "More frequent trips to gas station"
            },
            {
                'id': 'overheating',
                'question': "Is the engine overheating?",
                'options': ['Yes', 'No'],
                'hint': "Temperature gauge in red zone"
            },
            {
                'id': 'coolant_leak',
                'question': "Do you see coolant leaks under the car?",
                'options': ['Yes', 'No'],
                'hint': "Green/colored puddle under parked car"
            },
            {
                'id': 'brake_noise',
                'question': "Do you hear noise when braking?",
                'options': ['Yes', 'No'],
                'hint': "Squealing, grinding, or scraping sounds"
            },
            {
                'id': 'vibration_while_braking',
                'question': "Do you feel vibration when braking?",
                'options': ['Yes', 'No'],
                'hint': "Steering wheel or pedal shakes during braking"
            },
            {
                'id': 'check_engine_light',
                'question': "Is the check engine light ON?",
                'options': ['Yes', 'No'],
                'hint': "Orange/yellow engine symbol on dashboard"
            },
            {
                'id': 'poor_performance',
                'question': "Is overall performance poor?",
                'options': ['Yes', 'No'],
                'hint': "General lack of power or responsiveness"
            },
            {
                'id': 'steering_vibration',
                'question': "Do you feel vibration in steering wheel?",
                'options': ['Yes', 'No'],
                'hint': "Steering wheel shakes at certain speeds"
            },
            {
                'id': 'uneven_tire_wear',
                'question': "Are tires wearing unevenly?",
                'options': ['Yes', 'No'],
                'hint': "One side of tire more worn than other"
            },
            {
                'id': 'loud_exhaust',
                'question': "Is exhaust louder than normal?",
                'options': ['Yes', 'No'],
                'hint': "Unusual rumbling or roaring from exhaust"
            },
            {
                'id': 'decreased_power',
                'question': "Has engine power decreased?",
                'options': ['Yes', 'No'],
                'hint': "Car struggles on hills or with load"
            }
        ]

    def start_diagnosis(self):
        """Main interactive diagnosis procedure"""
        print("\n------------")
        print("INTERACTIVE CAR DIAGNOSTIC EXPERT SYSTEM")

        print("\nWelcome! I'll help diagnose your car problems.")
        print("Please answer the following questions about your car's symptoms.\n")

        # Collect car information
        self._collect_car_info()

        # Collect symptoms interactively
        self._collect_symptoms_interactive()

        # Apply rules and diagnose
        diagnoses = self._apply_rules()

        # Generate report
        self._generate_report(diagnoses)

        # Ask if user wants explanation
        self._offer_explanation()

        # Ask about repair
        self._offer_repair_advice()

    def _collect_car_info(self):
        """Collect basic car information"""
        print("First, let's get some basic information:")
        

        self.car_info = {}

        self.car_info['make'] = input("Car make (e.g., Toyota, Honda): ").strip()
        self.car_info['model'] = input("Car model (e.g., Corolla, Civic): ").strip()
        self.car_info['year'] = input("Year of manufacture: ").strip()
        self.car_info['mileage'] = input("Current mileage (km): ").strip()

        print("\nThanks! Now let's talk about the problems you're experiencing.\n")

    def _collect_symptoms_interactive(self):
        """Interactive symptom collection with user-friendly interface"""
        print("Please describe your car's symptoms:")
        

        symptoms_collected = 0

        for i, q in enumerate(self.questions, 1):
            print(f"\n{i}: {q['question']}")
            if q.get('hint'):
                print(f"{q['hint']}")

            # Get user response
            while True:
                response = input(f" Enter {q['options'][0]}/{q['options'][1]}: ").strip().lower()

                if response in ['yes', 'y', 'true', '1']:
                    self.symptoms[q['id']] = True
                    symptoms_collected += 1
                    break
                elif response in ['no', 'n', 'false', '0']:
                    self.symptoms[q['id']] = False
                    break
                else:
                    print(f"   Please enter '{q['options'][0]}' or '{q['options'][1]}'")

        print(f"\n✓ Collected {symptoms_collected} symptoms")

    def _apply_rules(self):
        """Apply rule-based reasoning to symptoms"""
        diagnoses = []
        self.certainty_factors = {}

        print("\n" + "Analyzing symptoms...")
        

        for rule in self.rules:
            # Check if all conditions are met
            conditions_met = all(self.symptoms.get(cond, False) for cond in rule['if'])

            if conditions_met:
                cf = rule['cf']
                problem = rule['then']

                # Print which rule fired
                conditions_str = ' AND '.join(rule['if']).replace('_', ' ')
                print(f"Rule {rule['id']} fired: IF {conditions_str}")
                print(f"  Diagnosis: {problem} (CF={cf})")

                if problem in self.certainty_factors:
                    # Combine certainty factors
                    old_cf = self.certainty_factors[problem]['cf']
                    new_cf = old_cf + cf - (old_cf * cf)
                    self.certainty_factors[problem] = {
                        'cf': new_cf,
                        'rules': self.certainty_factors[problem]['rules'] + [rule['id']],
                        'action': rule['action'],
                        'cost': rule['cost_estimate']
                    }
                else:
                    self.certainty_factors[problem] = {
                        'cf': cf,
                        'rules': [rule['id']],
                        'action': rule['action'],
                        'cost': rule['cost_estimate']
                    }

                diagnoses.append({
                    'problem': problem,
                    'certainty': cf,
                    'action': rule['action'],
                    'cost': rule['cost_estimate'],
                    'rule': rule['id']
                })

        return sorted(diagnoses, key=lambda x: x['certainty'], reverse=True)

    def _generate_report(self, diagnoses):
        """Generate comprehensive diagnostic report"""

        print("DIAGNOSTIC REPORT")


        # Car info summary
        print(f"\nCar: {self.car_info.get('make', 'Unknown')} {self.car_info.get('model', 'Unknown')}")
        print(f"Year: {self.car_info.get('year', 'Unknown')}")
        print(f"Mileage: {self.car_info.get('mileage', 'Unknown')} km")

        # Symptom summary
        symptom_count = sum(1 for s in self.symptoms.values() if s)
        print(f"\nSymptoms reported: {symptom_count}/18")

        if not diagnoses:
            print("\n-----------")
            print("No specific problems identified.")
            print("\nRecommendations:")
            print("1. Basic maintenance check")
            print("2. Oil change if due")
            print("3. Tire pressure check")
            return

        print(f"\nProblems identified: {len(diagnoses)}")
        print("\n-------------")

        # Show top diagnoses
        for i, diag in enumerate(diagnoses[:3], 1):
            problem = diag['problem']
            cf_data = self.certainty_factors.get(problem, {})
            certainty = cf_data.get('cf', diag['certainty']) * 100

            # Determine severity
            if certainty > 80:
                severity = "HIGH"
            elif certainty > 50:
                severity = "MEDIUM"
            else:
                severity = "LOW"

            print(f"\n{i}. {problem.upper()}")
            print(f"   Confidence: {certainty:.1f}%")
            print(f"   Severity: {severity}")
            print(f"   Action: {diag['action']}")
            print(f"   Estimated Cost: {diag['cost']}")

            # Show contributing symptoms
            rule_ids = cf_data.get('rules', [diag['rule']])
            for rule_id in rule_ids[:2]:  # Show up to 2 rules
                rule = next((r for r in self.rules if r['id'] == rule_id), None)
                if rule:
                    conditions = ' AND '.join(rule['if']).replace('_', ' ')
                    print(f"   Reason: {conditions}")

        # Overall assessment
        print("\n---------")
        if diagnoses[0]['certainty'] > 0.7:
            print("URGENT ATTENTION REQUIRED!")
            print("• Safety may be compromised")
            print("• Repair immediately")
        elif diagnoses[0]['certainty'] > 0.4:
            print("SCHEDULE REPAIR SOON")
            print("• Problem detected")
            print("• Schedule within 1-2 weeks")
        else:
            print("MONITOR AND MAINTAIN")
            print("• Minor issue detected")
            print("• Address during next service")

    def _offer_explanation(self):
        """Offer to explain reasoning"""
        if not self.certainty_factors:
            return

        response = input("\n Would you like to see detailed reasoning? (yes/no): ").lower()

        if response in ['yes', 'y']:
            print("\n------------")
            print("REASONING EXPLANATION")


            for problem, data in self.certainty_factors.items():
                print(f"\nFor '{problem}':")
                print(f"  Final Confidence: {data['cf']*100:.1f}%")

                # Show all contributing rules
                for rule_id in data['rules']:
                    rule = next((r for r in self.rules if r['id'] == rule_id), None)
                    if rule:
                        conditions = ' AND '.join(rule['if']).replace('_', ' ')
                        print(f"  • Rule {rule_id}: IF {conditions}")
                        print(f"      THEN {rule['then']} (CF={rule['cf']})")

                print(f"  Recommended Action: {data['action']}")
                print(f"  Estimated Cost: {data['cost']}")

    def _offer_repair_advice(self):
        """Offer repair and maintenance advice"""
        response = input("\nWould you like general car maintenance advice? (yes/no): ").lower()

        if response in ['yes', 'y']:

            print("GENERAL CAR MAINTENANCE ADVICE")


            mileage = int(self.car_info.get('mileage', 0)) if self.car_info.get('mileage', '').isdigit() else 0

            print("\nBased on your car's information:")

            if mileage > 100000:
                print("HIGH MILEAGE (>100,000 km):")
                print("  - Check timing belt/chain replacement")
                print("  - Inspect suspension components")
                print("  - Consider transmission fluid change")
            elif mileage > 50000:
                print("MEDIUM MILEAGE (50,000-100,000 km):")
                print("  - Change coolant and brake fluid")
                print("  - Inspect brakes and tires")
                print("  - Check battery health")
            else:
                print("•LOW MILEAGE (<50,000 km):")
                print("  - Regular oil changes")
                print("  - Check tire pressure monthly")
                print("  - Keep up with scheduled maintenance")

            # Specific advice based on symptoms
            if self.symptoms.get('high_fuel_consumption', False):
                print("\nFOR FUEL EFFICIENCY:")
                print("  - Check tire pressure (low pressure increases fuel use)")
                print("  - Clean air filter")
                print("  - Use recommended fuel grade")

            if self.symptoms.get('brake_noise', False) or self.symptoms.get('vibration_while_braking', False):
                print("\nBRAKE SAFETY:")
                print("  - Brakes are critical for safety")
                print("  - Don't delay brake repairs")
                print("  - Get professional inspection")

    def run_quick_test(self):
        """Quick diagnostic test for common problems"""

        print("QUICK DIAGNOSTIC TEST")

        print("\nAnswer 3 key questions for quick assessment:\n")

        quick_questions = [
            ("engine_wont_start", "Does the engine not start?"),
            ("check_engine_light", "Is check engine light ON?"),
            ("brake_noise", "Any brake noise or issues?")
        ]

        quick_symptoms = {}
        for symptom_id, question in quick_questions:
            response = input(f"{question} (yes/no): ").lower()
            quick_symptoms[symptom_id] = response in ['yes', 'y']

        # Quick analysis
        print("\n---------------")
        print("QUICK ASSESSMENT:")

        if quick_symptoms.get('engine_wont_start'):
            print("Starting problem detected")
            print("  - Check battery and starter")
        if quick_symptoms.get('check_engine_light'):
            print("Check engine light ON")
            print("  - Get OBD-II diagnostic scan")
        if quick_symptoms.get('brake_noise'):
            print("Brake issue detected")
            print("  - Immediate inspection recommended")

        if not any(quick_symptoms.values()):
            print("• No major issues detected in quick test")
            print("  - Continue with full diagnosis if problems persist")

# Main execution
def run_interactive_car_diagnostic():
    """Run the interactive car diagnostic system"""
    expert = InteractiveCarDiagnosticExpert()


    print("SELECT DIAGNOSTIC MODE:")

    print("1. Full Interactive Diagnosis")
    print("2. Quick Diagnostic Test")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == '1':
        expert.start_diagnosis()
    elif choice == '2':
        expert.run_quick_test()
        # Ask if they want full diagnosis after quick test
        response = input("\nRun full diagnosis? (yes/no): ").lower()
        if response in ['yes', 'y']:
            expert.start_diagnosis()
    elif choice == '3':
        print("\nThank you for using Car Diagnostic Expert System!")
    else:
        print("Invalid choice. Running full diagnosis...")
        expert.start_diagnosis()

    # Farewell
    print("Thank you for using our Car Diagnostic System!")
    print("Drive safely!")


# Run the system
if __name__ == "__main__":
    run_interactive_car_diagnostic()

