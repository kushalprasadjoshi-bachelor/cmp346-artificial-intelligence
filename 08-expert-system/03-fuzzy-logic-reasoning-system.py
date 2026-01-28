# Question: Implement the fuzzy logic for reasoning in an expert system.

"""
FUZZY LOGIC REASONING SYSTEM - FIXED VERSION
With proper print handling and matplotlib fixes
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Import matplotlib with non-interactive backend for saving files
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

class FuzzyReasoningExpertSystem:
    """Expert system using ONLY fuzzy logic for reasoning"""

    def __init__(self):
        self.setup_system()

    def setup_system(self):
        """Setup fuzzy variables and rules"""
        print("Initializing fuzzy system...", end="")

        # ----- INPUT VARIABLES -----

        # 1. Temperature (in Celsius)
        self.temperature = ctrl.Antecedent(np.arange(35, 42, 0.1), 'temperature')
        self.temperature['low'] = fuzz.trimf(self.temperature.universe, [35, 35, 37])
        self.temperature['normal'] = fuzz.trimf(self.temperature.universe, [36, 37, 38])
        self.temperature['high'] = fuzz.trimf(self.temperature.universe, [37, 39, 42])
        self.temperature['very_high'] = fuzz.trimf(self.temperature.universe, [38.5, 41, 42])

        # 2. Cough severity (0-10 scale)
        self.cough = ctrl.Antecedent(np.arange(0, 11, 1), 'cough')
        self.cough['none'] = fuzz.trimf(self.cough.universe, [0, 0, 2])
        self.cough['mild'] = fuzz.trimf(self.cough.universe, [1, 3, 5])
        self.cough['moderate'] = fuzz.trimf(self.cough.universe, [4, 6, 8])
        self.cough['severe'] = fuzz.trimf(self.cough.universe, [7, 10, 10])

        # 3. Fatigue level (0-10 scale)
        self.fatigue = ctrl.Antecedent(np.arange(0, 11, 1), 'fatigue')
        self.fatigue['low'] = fuzz.trimf(self.fatigue.universe, [0, 0, 4])
        self.fatigue['medium'] = fuzz.trimf(self.fatigue.universe, [3, 5, 7])
        self.fatigue['high'] = fuzz.trimf(self.fatigue.universe, [6, 10, 10])

        # ----- OUTPUT VARIABLES (Disease Risks) -----

        # Flu Risk
        self.flu_risk = ctrl.Consequent(np.arange(0, 101, 1), 'flu_risk')
        self.flu_risk['very_low'] = fuzz.trimf(self.flu_risk.universe, [0, 0, 25])
        self.flu_risk['low'] = fuzz.trimf(self.flu_risk.universe, [0, 25, 50])
        self.flu_risk['medium'] = fuzz.trimf(self.flu_risk.universe, [25, 50, 75])
        self.flu_risk['high'] = fuzz.trimf(self.flu_risk.universe, [50, 75, 100])
        self.flu_risk['very_high'] = fuzz.trimf(self.flu_risk.universe, [75, 100, 100])

        # COVID Risk
        self.covid_risk = ctrl.Consequent(np.arange(0, 101, 1), 'covid_risk')
        self.covid_risk['very_low'] = fuzz.trimf(self.covid_risk.universe, [0, 0, 20])
        self.covid_risk['low'] = fuzz.trimf(self.covid_risk.universe, [10, 30, 50])
        self.covid_risk['medium'] = fuzz.trimf(self.covid_risk.universe, [40, 60, 80])
        self.covid_risk['high'] = fuzz.trimf(self.covid_risk.universe, [70, 85, 100])
        self.covid_risk['very_high'] = fuzz.trimf(self.covid_risk.universe, [90, 100, 100])

        # Common Cold Risk
        self.cold_risk = ctrl.Consequent(np.arange(0, 101, 1), 'cold_risk')
        self.cold_risk['very_low'] = fuzz.trimf(self.cold_risk.universe, [0, 0, 30])
        self.cold_risk['low'] = fuzz.trimf(self.cold_risk.universe, [20, 40, 60])
        self.cold_risk['medium'] = fuzz.trimf(self.cold_risk.universe, [50, 65, 80])
        self.cold_risk['high'] = fuzz.trimf(self.cold_risk.universe, [70, 85, 100])
        self.cold_risk['very_high'] = fuzz.trimf(self.cold_risk.universe, [90, 100, 100])

        # ----- FUZZY RULES FOR REASONING -----

        # FLU RULES (Fuzzy reasoning about flu)
        rule1 = ctrl.Rule(self.temperature['high'] & self.cough['severe'],
                         self.flu_risk['very_high'])
        rule2 = ctrl.Rule(self.temperature['high'] & self.cough['moderate'],
                         self.flu_risk['high'])
        rule3 = ctrl.Rule(self.temperature['normal'] & self.cough['severe'] & self.fatigue['high'],
                         self.flu_risk['high'])
        rule4 = ctrl.Rule(self.temperature['normal'] & self.cough['mild'],
                         self.flu_risk['medium'])
        rule5 = ctrl.Rule(self.temperature['low'] | self.cough['none'],
                         self.flu_risk['very_low'])

        # COVID RULES (Fuzzy reasoning about COVID)
        rule6 = ctrl.Rule(self.temperature['very_high'] & self.fatigue['high'],
                         self.covid_risk['very_high'])
        rule7 = ctrl.Rule(self.temperature['high'] & self.cough['moderate'],
                         self.covid_risk['high'])
        rule8 = ctrl.Rule(self.temperature['normal'] & self.fatigue['medium'],
                         self.covid_risk['medium'])

        # COLD RULES (Fuzzy reasoning about cold)
        rule9 = ctrl.Rule(self.temperature['normal'] & self.cough['mild'],
                         self.cold_risk['high'])
        rule10 = ctrl.Rule(self.temperature['low'] & self.cough['moderate'],
                          self.cold_risk['medium'])

        # ----- CREATE SEPARATE CONTROL SYSTEMS -----
        flu_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
        covid_ctrl = ctrl.ControlSystem([rule6, rule7, rule8])
        cold_ctrl = ctrl.ControlSystem([rule9, rule10])

        # Create simulation objects
        self.flu_sim = ctrl.ControlSystemSimulation(flu_ctrl)
        self.covid_sim = ctrl.ControlSystemSimulation(covid_ctrl)
        self.cold_sim = ctrl.ControlSystemSimulation(cold_ctrl)

        print(" ✓ DONE")

    def diagnose(self, temp, cough_level, fatigue_level):
        """Perform fuzzy reasoning diagnosis"""

        results = {}

        # ---- FLU ----
        self.flu_sim.input['temperature'] = temp
        self.flu_sim.input['cough'] = cough_level
        self.flu_sim.input['fatigue'] = fatigue_level
        self.flu_sim.compute()
        results['flu'] = self.flu_sim.output.get('flu_risk', 0)

        # ---- COVID ----
        self.covid_sim.input['temperature'] = temp
        self.covid_sim.input['cough'] = cough_level
        self.covid_sim.input['fatigue'] = fatigue_level
        self.covid_sim.compute()
        results['covid'] = self.covid_sim.output.get('covid_risk', 0)

        # ---- COLD ----
        self.cold_sim.input['temperature'] = temp
        self.cold_sim.input['cough'] = cough_level
        self.cold_sim.compute()
        results['cold'] = self.cold_sim.output.get('cold_risk', 0)

        return results

    def explain_reasoning(self, temp, cough_level, fatigue_level):
        """Explain the fuzzy reasoning process"""

        print("\n" + "=" * 60)
        print("FUZZY REASONING EXPLANATION")
        print("=" * 60)

        print(f"\nInput Values:")
        print(f"  Temperature: {temp}°C")
        print(f"  Cough Level: {cough_level}/10")
        print(f"  Fatigue Level: {fatigue_level}/10")

        print(f"\n1. FUZZIFICATION (Crisp → Fuzzy):")

        # Calculate membership degrees
        temp_degrees = {}
        for term in ['low', 'normal', 'high', 'very_high']:
            membership = fuzz.interp_membership(self.temperature.universe,
                                                self.temperature[term].mf,
                                                temp)
            if membership > 0.01:
                # Convert numpy float to regular float for cleaner display
                temp_degrees[term] = float(round(membership, 3))

        cough_degrees = {}
        for term in ['none', 'mild', 'moderate', 'severe']:
            membership = fuzz.interp_membership(self.cough.universe,
                                                self.cough[term].mf,
                                                cough_level)
            if membership > 0.01:
                cough_degrees[term] = float(round(membership, 3))

        fatigue_degrees = {}
        for term in ['low', 'medium', 'high']:
            membership = fuzz.interp_membership(self.fatigue.universe,
                                                self.fatigue[term].mf,
                                                fatigue_level)
            if membership > 0.01:
                fatigue_degrees[term] = float(round(membership, 3))

        print(f"  Temperature: {temp_degrees}")
        print(f"  Cough: {cough_degrees}")
        print(f"  Fatigue: {fatigue_degrees}")

        # More detailed explanation
        print(f"\nInterpretation:")
        for term, degree in temp_degrees.items():
            print(f"  • Temperature is {term} (confidence: {degree * 100:.0f}%)")

        for term, degree in cough_degrees.items():
            print(f"  • Cough is {term} (confidence: {degree * 100:.0f}%)")

        for term, degree in fatigue_degrees.items():
            print(f"  • Fatigue is {term} (confidence: {degree * 100:.0f}%)")


        print(f"\n2. RULE EVALUATION (Mamdani Inference):")

        # Get actual outputs for verification
        results = self.diagnose(temp, cough_level, fatigue_level)
        print(f"\n3. FINAL RESULTS (After Defuzzification):")
        for disease, risk in results.items():
            print(f"   - {disease.upper()}: {risk:.1f}%")

    def visualize_fuzzy_sets(self):
        """Visualize the fuzzy membership functions"""
        print("\nGenerating visualization...", end="")

        fig, axes = plt.subplots(3, 3, figsize=(15, 12))

        # Temperature
        axes[0, 0].plot(self.temperature.universe, self.temperature['low'].mf, 'b', linewidth=2, label='Low')
        axes[0, 0].plot(self.temperature.universe, self.temperature['normal'].mf, 'g', linewidth=2, label='Normal')
        axes[0, 0].plot(self.temperature.universe, self.temperature['high'].mf, 'r', linewidth=2, label='High')
        axes[0, 0].plot(self.temperature.universe, self.temperature['very_high'].mf, 'm', linewidth=2, label='Very High')
        axes[0, 0].set_title('Temperature (°C)', fontsize=12, fontweight='bold')
        axes[0, 0].set_xlabel('Temperature (°C)')
        axes[0, 0].set_ylabel('Membership')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # Cough
        axes[0, 1].plot(self.cough.universe, self.cough['none'].mf, 'b', linewidth=2, label='None')
        axes[0, 1].plot(self.cough.universe, self.cough['mild'].mf, 'g', linewidth=2, label='Mild')
        axes[0, 1].plot(self.cough.universe, self.cough['moderate'].mf, 'r', linewidth=2, label='Moderate')
        axes[0, 1].plot(self.cough.universe, self.cough['severe'].mf, 'm', linewidth=2, label='Severe')
        axes[0, 1].set_title('Cough Severity (0-10)', fontsize=12, fontweight='bold')
        axes[0, 1].set_xlabel('Cough Level')
        axes[0, 1].set_ylabel('Membership')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)

        # Fatigue
        axes[0, 2].plot(self.fatigue.universe, self.fatigue['low'].mf, 'b', linewidth=2, label='Low')
        axes[0, 2].plot(self.fatigue.universe, self.fatigue['medium'].mf, 'g', linewidth=2, label='Medium')
        axes[0, 2].plot(self.fatigue.universe, self.fatigue['high'].mf, 'r', linewidth=2, label='High')
        axes[0, 2].set_title('Fatigue Level (0-10)', fontsize=12, fontweight='bold')
        axes[0, 2].set_xlabel('Fatigue Level')
        axes[0, 2].set_ylabel('Membership')
        axes[0, 2].legend()
        axes[0, 2].grid(True, alpha=0.3)

        # Flu Risk
        axes[1, 0].plot(self.flu_risk.universe, self.flu_risk['very_low'].mf, 'b', linewidth=2, label='Very Low')
        axes[1, 0].plot(self.flu_risk.universe, self.flu_risk['low'].mf, 'g', linewidth=2, label='Low')
        axes[1, 0].plot(self.flu_risk.universe, self.flu_risk['medium'].mf, 'r', linewidth=2, label='Medium')
        axes[1, 0].plot(self.flu_risk.universe, self.flu_risk['high'].mf, 'm', linewidth=2, label='High')
        axes[1, 0].plot(self.flu_risk.universe, self.flu_risk['very_high'].mf, 'c', linewidth=2, label='Very High')
        axes[1, 0].set_title('Flu Risk (%)', fontsize=12, fontweight='bold')
        axes[1, 0].set_xlabel('Risk Percentage')
        axes[1, 0].set_ylabel('Membership')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)

        # COVID Risk
        axes[1, 1].plot(self.covid_risk.universe, self.covid_risk['very_low'].mf, 'b', linewidth=2, label='Very Low')
        axes[1, 1].plot(self.covid_risk.universe, self.covid_risk['low'].mf, 'g', linewidth=2, label='Low')
        axes[1, 1].plot(self.covid_risk.universe, self.covid_risk['medium'].mf, 'r', linewidth=2, label='Medium')
        axes[1, 1].plot(self.covid_risk.universe, self.covid_risk['high'].mf, 'm', linewidth=2, label='High')
        axes[1, 1].plot(self.covid_risk.universe, self.covid_risk['very_high'].mf, 'c', linewidth=2, label='Very High')
        axes[1, 1].set_title('COVID Risk (%)', fontsize=12, fontweight='bold')
        axes[1, 1].set_xlabel('Risk Percentage')
        axes[1, 1].set_ylabel('Membership')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)

        # Cold Risk
        axes[1, 2].plot(self.cold_risk.universe, self.cold_risk['very_low'].mf, 'b', linewidth=2, label='Very Low')
        axes[1, 2].plot(self.cold_risk.universe, self.cold_risk['low'].mf, 'g', linewidth=2, label='Low')
        axes[1, 2].plot(self.cold_risk.universe, self.cold_risk['medium'].mf, 'r', linewidth=2, label='Medium')
        axes[1, 2].plot(self.cold_risk.universe, self.cold_risk['high'].mf, 'm', linewidth=2, label='High')
        axes[1, 2].plot(self.cold_risk.universe, self.cold_risk['very_high'].mf, 'c', linewidth=2, label='Very High')
        axes[1, 2].set_title('Cold Risk (%)', fontsize=12, fontweight='bold')
        axes[1, 2].set_xlabel('Risk Percentage')
        axes[1, 2].set_ylabel('Membership')
        axes[1, 2].legend()
        axes[1, 2].grid(True, alpha=0.3)

        # Hide empty subplots
        axes[2, 0].axis('off')
        axes[2, 1].axis('off')
        axes[2, 2].axis('off')

        # Add text explanation in empty subplots
        axes[2, 0].text(0.5, 0.5, 'Fuzzy Reasoning Process:\n\n1. Fuzzification\n2. Rule Evaluation\n3. Aggregation\n4. Defuzzification',
                       horizontalalignment='center', verticalalignment='center',
                       fontsize=12, transform=axes[2, 0].transAxes)

        plt.suptitle('Fuzzy Sets for Medical Diagnosis Expert System', fontsize=16, fontweight='bold')
        plt.tight_layout()

        # Save the figure
        filename = 'fuzzy_reasoning_sets.png'
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close(fig)  # Close the figure to free memory

        print(" ✓ DONE")
        print(f"\n✓ Visualization saved as '{filename}'")
        print("  You can find it in your current working directory.")
        return filename

    def interactive_diagnosis(self):
        """Interactive fuzzy reasoning diagnosis"""
        print("\n" + "="*60)
        print("FUZZY LOGIC EXPERT SYSTEM - INTERACTIVE MODE")
        print("="*60)

        # Get inputs
        while True:
            try:
                temp = float(input("\nEnter temperature (°C, 35-42): "))
                if 35 <= temp <= 42:
                    break
                else:
                    print("Temperature must be between 35-42°C")
            except ValueError:
                print("Please enter a valid number")

        while True:
            try:
                cough = float(input("Enter cough severity (0-10): "))
                if 0 <= cough <= 10:
                    break
                else:
                    print("Cough severity must be between 0-10")
            except ValueError:
                print("Please enter a valid number")

        while True:
            try:
                fatigue = float(input("Enter fatigue level (0-10): "))
                if 0 <= fatigue <= 10:
                    break
                else:
                    print("Fatigue level must be between 0-10")
            except ValueError:
                print("Please enter a valid number")

        print("\n" + "="*60)
        print("FUZZY REASONING IN PROGRESS...")
        print("="*60)

        # Perform diagnosis
        results = self.diagnose(temp, cough, fatigue)

        # Show results
        print("\nDIAGNOSIS RESULTS:")
        print("-"*50)

        for disease, risk in results.items():
            # Linguistic interpretation
            if risk >= 80:
                interpretation = "VERY HIGH RISK"
                emoji = "🚨"
            elif risk >= 60:
                interpretation = "HIGH RISK"
                emoji = "⚠️"
            elif risk >= 40:
                interpretation = "MEDIUM RISK"
                emoji = "🔶"
            elif risk >= 20:
                interpretation = "LOW RISK"
                emoji = "🔷"
            else:
                interpretation = "VERY LOW RISK"
                emoji = "✅"

            print(f"{emoji} {disease.upper()}: {risk:.1f}% ({interpretation})")

        # Determine primary diagnosis
        primary = max(results.items(), key=lambda x: x[1])
        print(f"\n🎯 PRIMARY DIAGNOSIS: {primary[0].upper()} ({primary[1]:.1f}% risk)")

        # Offer explanation
        if input("\nShow detailed fuzzy reasoning steps? (yes/no): ").lower() in ['yes', 'y']:
            self.explain_reasoning(temp, cough, fatigue)

    def run_demo_cases(self):
        """Run demonstration test cases"""
        print("\n" + "="*60)
        print("DEMONSTRATION: Fuzzy Reasoning Examples")
        print("="*60)

        test_cases = [
            ("Severe Flu Case", 39.5, 8, 9),
            ("Moderate COVID Case", 38.8, 6, 8),
            ("Mild Cold Case", 37.2, 4, 3),
            ("Normal Case", 36.5, 2, 2),
            ("Critical Case", 40.5, 9, 10)
        ]

        for case_name, temp, cough, fatigue in test_cases:
            print(f"\n{'='*40}")
            print(f"CASE: {case_name}")
            print(f"{'='*40}")
            print(f"Temperature: {temp}°C")
            print(f"Cough: {cough}/10")
            print(f"Fatigue: {fatigue}/10")

            results = self.diagnose(temp, cough, fatigue)

            print("\nFuzzy Reasoning Results:")
            for disease, risk in results.items():
                print(f"  {disease.upper()}: {risk:.1f}%")

            primary = max(results.items(), key=lambda x: x[1])
            print(f"\n  → Conclusion: {primary[0].upper()} (Highest risk)")

def display_help():
    """Display help information about fuzzy reasoning"""
    print("\n" + "="*60)
    print("ABOUT FUZZY REASONING IN EXPERT SYSTEMS")
    print("="*60)

    help_text = """
FUZZY LOGIC REASONING PROCESS:

1. FUZZIFICATION:
   - Convert crisp inputs (e.g., 39°C) to fuzzy sets
   - Example: 39°C → High: 0.8, Very High: 0.2

2. FUZZY RULES:
   - IF-THEN rules with linguistic variables
   - Example: IF temperature IS high AND cough IS severe
              THEN flu_risk IS very_high

3. INFERENCE (Mamdani Method):
   - Apply rules to fuzzy inputs
   - Use min() for AND, max() for OR
   - Clip output membership functions at rule strength

4. AGGREGATION:
   - Combine outputs from all fired rules
   - Take union (max) of clipped outputs

5. DEFUZZIFICATION (Centroid Method):
   - Convert fuzzy output to crisp value
   - Output = ∫ μ(x)·x dx / ∫ μ(x) dx
   - Example: flu_risk = 85.3%

KEY DIFFERENCE FROM RULE-BASED SYSTEMS:
- Rule-based: IF fever=True AND cough=True THEN flu (CF=0.7)
- Fuzzy logic: IF temp IS high AND cough IS severe THEN flu_risk IS high
"""
    print(help_text)

    print("\nLIBRARIES USED:")
    print("-"*40)
    print("1. NumPy: Numerical computations")
    print("2. SciKit-Fuzzy: Fuzzy logic toolkit")
    print("3. Matplotlib: Visualization")

    print("\nINSTALLATION (if not installed):")
    print("-"*40)
    print("pip install numpy scikit-fuzzy matplotlib")

def clear_screen():
    """Clear the screen (platform independent)"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    """Main function to run the fuzzy reasoning expert system"""
    # Clear screen at start
    clear_screen()

    print("\n" + "="*70)
    print("IMPLEMENTING FUZZY LOGIC FOR REASONING IN EXPERT SYSTEM")
    print("="*70)
    print("\nThis program demonstrates PURE fuzzy logic reasoning (not hybrid).")
    print("It shows the complete fuzzy inference process from input to output.")

    # Initialize system
    print("\nInitializing Fuzzy Reasoning Expert System...")
    expert = FuzzyReasoningExpertSystem()

    # Main menu loop
    while True:
        print("\n" + "="*60)
        print("MAIN MENU")
        print("="*60)
        print("\n1. 🩺 Interactive Diagnosis")
        print("2. 🧪 Run Demonstration Cases")
        print("3. 📊 Visualize Fuzzy Sets")
        print("4. 📚 Learn About Fuzzy Reasoning")
        print("5. 🏃 Run Quick Test")
        print("6. ❌ Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            expert.interactive_diagnosis()
            input("\nPress Enter to continue...")

        elif choice == '2':
            expert.run_demo_cases()
            input("\nPress Enter to continue...")

        elif choice == '3':
            print("\nGenerating visualization of fuzzy sets...")
            filename = expert.visualize_fuzzy_sets()
            print(f"\n✓ File saved successfully: {filename}")
            print("  The image shows all fuzzy membership functions used in the system.")
            input("\nPress Enter to continue...")

        elif choice == '4':
            display_help()
            input("\nPress Enter to continue...")

        elif choice == '5':
            # Quick test
            print("\n" + "="*60)
            print("QUICK TEST")
            print("="*60)
            print("\nRunning quick test with sample data...")

            # Test with sample data
            test_data = (38.5, 7, 8)  # temp, cough, fatigue
            results = expert.diagnose(*test_data)

            print(f"\nInput: Temperature={test_data[0]}°C, Cough={test_data[1]}/10, Fatigue={test_data[2]}/10")
            print("\nResults:")
            for disease, risk in results.items():
                print(f"  {disease.upper()}: {risk:.1f}%")

            primary = max(results.items(), key=lambda x: x[1])
            print(f"\nPrimary Diagnosis: {primary[0].upper()} ({primary[1]:.1f}% risk)")
            input("\nPress Enter to continue...")

        elif choice == '6':
            print("\n" + "="*60)
            print("Thank you for using the Fuzzy Logic Reasoning Expert System!")
            print("="*60)
            break

        else:
            print("\n❌ Invalid choice. Please enter a number between 1-6.")
            input("Press Enter to continue...")

        # Clear screen for next iteration
        clear_screen()

# Run the program
if __name__ == "__main__":
    try:
        # Check for required libraries
        import numpy as np
        import skfuzzy
        import matplotlib.pyplot as plt

        print("✓ All required libraries are available.")
        main()

    except ImportError as e:
        print(f"\n❌ Error: Missing required library - {e}")
        print("\nPlease install required libraries using:")
        print("\nFor pip:")
        print("pip install numpy scikit-fuzzy matplotlib")
        print("\nFor conda:")
        print("conda install numpy scikit-fuzzy matplotlib")

        # Try to install automatically (optional)
        install = input("\nAttempt automatic installation? (yes/no): ").lower()
        if install in ['yes', 'y']:
            import subprocess
            import sys

            print("\nInstalling required libraries...")
            subprocess.check_call([sys.executable, "-m", "pip", "install",
                                  "numpy", "scikit-fuzzy", "matplotlib"])
            print("\n✓ Installation complete! Restarting program...")
            main()


