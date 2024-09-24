# election_game.py

def display_status(scenario_number, inflation, unemployment, approval):
    print(f"\n--- Scenario {scenario_number} ---")
    print(f"Inflation Rate: {inflation:.1f}%")
    print(f"Unemployment Rate: {unemployment:.1f}%")
    print(f"Approval Rating: {approval}%")

def get_player_choice(options):
    print("\nChoose a policy option:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option['description']}")
    choice = input("Enter the number of your choice: ")
    while choice not in [str(i) for i in range(1, len(options)+1)]:
        choice = input(f"Invalid choice. Please enter a number between 1 and {len(options)}: ")
    return int(choice) - 1

def apply_policy(choice_effects, inflation, unemployment, approval):
    inflation_change = choice_effects['inflation']
    unemployment_change = choice_effects['unemployment']
    approval_change = choice_effects['approval']

    inflation += inflation_change
    unemployment += unemployment_change
    approval += approval_change

    # Ensure values stay within realistic bounds
    inflation = max(-5.0, min(15.0, inflation))
    unemployment = max(0.0, min(25.0, unemployment))
    approval = max(0, min(100, approval))

    return inflation, unemployment, approval

def main():
    # Initial conditions
    inflation = 3.0
    unemployment = 5.0
    approval = 50
    scenario_number = 1

    # Define scenarios
    scenarios = [
        # Scenario 1: Oil Price Shock
        {
            'situation': "A sudden increase in global oil prices is leading to higher production costs and consumer prices.",
            'options': [
                {
                    'description': "Subsidize Fuel Costs",
                    'effects': {'inflation': -1.0, 'unemployment': 0.0, 'approval': +3},
                    'explanation': "Government absorbs some of the cost, easing inflation but increasing the budget deficit."
                },
                {
                    'description': "Promote Energy Conservation",
                    'effects': {'inflation': -0.5, 'unemployment': +0.5, 'approval': +2},
                    'explanation': "Encourages reduced energy use, lowering demand and prices."
                },
                {
                    'description': "Invest in Alternative Energy",
                    'effects': {'inflation': +0.5, 'unemployment': -1.0, 'approval': +4},
                    'explanation': "Long-term solution that may stimulate the economy and reduce future inflation."
                },
            ]
        },
        # Scenario 2: Housing Market Collapse
        {
            'situation': "The housing market is experiencing a downturn, leading to reduced construction activity and job losses.",
            'options': [
                {
                    'description': "Implement Housing Stimulus",
                    'effects': {'inflation': +0.5, 'unemployment': -1.5, 'approval': +3},
                    'explanation': "Stimulating the housing market boosts employment but may raise inflation."
                },
                {
                    'description': "Offer Tax Credits to Homebuyers",
                    'effects': {'inflation': +0.2, 'unemployment': -1.0, 'approval': +2},
                    'explanation': "Encourages home purchases, supporting the market and jobs."
                },
                {
                    'description': "Allow Market Correction",
                    'effects': {'inflation': -0.5, 'unemployment': +1.0, 'approval': -2},
                    'explanation': "Non-intervention may stabilize prices but leads to higher unemployment."
                },
            ]
        },
        # Scenario 3: Currency Appreciation
        {
            'situation': "The national currency is appreciating rapidly, making exports more expensive and imports cheaper.",
            'options': [
                {
                    'description': "Intervene in Currency Markets",
                    'effects': {'inflation': +1.0, 'unemployment': -1.0, 'approval': +1},
                    'explanation': "Weakening the currency helps exporters but can increase inflation."
                },
                {
                    'description': "Reduce Interest Rates",
                    'effects': {'inflation': +0.5, 'unemployment': -0.5, 'approval': +1},
                    'explanation': "Lower rates make borrowing cheaper, stimulating the economy but may weaken the currency."
                },
                {
                    'description': "No Intervention",
                    'effects': {'inflation': -0.5, 'unemployment': +1.0, 'approval': -2},
                    'explanation': "Allowing the currency to appreciate may hurt employment."
                },
            ]
        },
        # Scenario 4: Agricultural Shortage
        {
            'situation': "A drought has reduced agricultural output, leading to higher food prices.",
            'options': [
                {
                    'description': "Import Food Supplies",
                    'effects': {'inflation': -1.0, 'unemployment': +0.5, 'approval': +2},
                    'explanation': "Addresses immediate shortages but may harm domestic agriculture."
                },
                {
                    'description': "Provide Aid to Farmers",
                    'effects': {'inflation': 0.0, 'unemployment': 0.0, 'approval': +3},
                    'explanation': "Supports farmers, maintains employment, but doesn't lower food prices."
                },
                {
                    'description': "Implement Price Controls on Food",
                    'effects': {'inflation': -0.5, 'unemployment': +1.0, 'approval': +2},
                    'explanation': "Short-term relief but may lead to shortages."
                },
            ]
        },
        # Scenario 5: Technological Innovation Boom
        {
            'situation': "A surge in technological innovation is automating jobs, increasing productivity but leading to job displacement.",
            'options': [
                {
                    'description': "Invest in Education and Training",
                    'effects': {'inflation': +0.5, 'unemployment': -1.5, 'approval': +4},
                    'explanation': "Prepares workforce for new jobs, boosting future employment."
                },
                {
                    'description': "Tax Automation",
                    'effects': {'inflation': +1.0, 'unemployment': -1.0, 'approval': +2},
                    'explanation': "Slows automation, preserves jobs, but may hinder innovation."
                },
                {
                    'description': "Encourage Technological Advancement",
                    'effects': {'inflation': -0.5, 'unemployment': +1.0, 'approval': -2},
                    'explanation': "Focuses on long-term economic growth at the expense of short-term employment."
                },
            ]
        },
        # Scenario 6: Financial Market Instability
        {
            'situation': "Volatility in financial markets is causing uncertainty, affecting investment and economic growth.",
            'options': [
                {
                    'description': "Implement Regulatory Reforms",
                    'effects': {'inflation': 0.0, 'unemployment': +0.5, 'approval': +3},
                    'explanation': "Aims to stabilize markets, may slow economic activity."
                },
                {
                    'description': "Provide Stimulus to Financial Institutions",
                    'effects': {'inflation': +0.5, 'unemployment': -0.5, 'approval': -2},
                    'explanation': "Supports markets, but may be unpopular."
                },
                {
                    'description': "Establish Public Investment Funds",
                    'effects': {'inflation': +0.3, 'unemployment': -0.5, 'approval': +2},
                    'explanation': "Government invests directly in the economy, promoting growth."
                },
            ]
        },
        # Scenario 7: Labor Strike Wave
        {
            'situation': "Multiple industries are experiencing strikes over wages and working conditions.",
            'options': [
                {
                    'description': "Mediate Negotiations",
                    'effects': {'inflation': +0.2, 'unemployment': 0.0, 'approval': +3},
                    'explanation': "Facilitates agreements, restoring production."
                },
                {
                    'description': "Legislate to Limit Strikes",
                    'effects': {'inflation': 0.0, 'unemployment': -0.5, 'approval': -3},
                    'explanation': "Forces workers back but harms approval."
                },
                {
                    'description': "Increase Minimum Wage",
                    'effects': {'inflation': +1.0, 'unemployment': +1.0, 'approval': +2},
                    'explanation': "Addresses wage concerns but risks inflation and unemployment."
                },
            ]
        },
        # Scenario 8: Natural Disaster Impact
        {
            'situation': "A major natural disaster has damaged infrastructure, disrupting economic activity.",
            'options': [
                {
                    'description': "Invest in Reconstruction",
                    'effects': {'inflation': +0.5, 'unemployment': -1.0, 'approval': +4},
                    'explanation': "Stimulates the economy, positive public sentiment."
                },
                {
                    'description': "Seek International Aid",
                    'effects': {'inflation': 0.0, 'unemployment': -0.5, 'approval': +2},
                    'explanation': "Brings in resources, lessens budget impact."
                },
                {
                    'description': "Implement Austerity to Fund Recovery",
                    'effects': {'inflation': -0.5, 'unemployment': +1.0, 'approval': -3},
                    'explanation': "Funds recovery without increasing debt but harms employment and approval."
                },
            ]
        },
    ]

    print("Welcome to the Election Game!")
    print("You are a politician running for election.")
    print("Make policy decisions to balance inflation and unemployment to win over voters.")
    print("You need an approval rating of 65% or higher after 8 scenarios to win the election.")
    print("Keep inflation between 1% and 5%, and unemployment at 6% or lower.")

    # Loop through scenarios
    for scenario in scenarios:
        display_status(scenario_number, inflation, unemployment, approval)
        print(f"\nSituation: {scenario['situation']}")
        choice_index = get_player_choice(scenario['options'])
        chosen_option = scenario['options'][choice_index]
        # Apply policy effects
        inflation, unemployment, approval = apply_policy(
            chosen_option['effects'],
            inflation,
            unemployment,
            approval
        )
        # Provide immediate feedback
        print(f"\nYou chose to: {chosen_option['description']}")
        print(f"Effects:")
        print(f"  Inflation Rate change: {chosen_option['effects']['inflation']}%")
        print(f"  Unemployment Rate change: {chosen_option['effects']['unemployment']}%")
        print(f"  Approval Rating change: {chosen_option['effects']['approval']}%")
        # Add explanation
        print(f"Explanation: {chosen_option['explanation']}")
        scenario_number += 1

    # Final evaluation
    print("\n--- Election Results ---")
    print(f"Final Inflation Rate: {inflation:.1f}%")
    print(f"Final Unemployment Rate: {unemployment:.1f}%")
    print(f"Final Approval Rating: {approval}%")

    # Determine outcome
    if (approval >= 65) and (1 <= inflation <= 5) and (unemployment <= 6):
        print("\nCongratulations! You have won the election!")
    else:
        print("\nUnfortunately, you did not meet the criteria to win the election.")
        if approval < 65:
            print(f"- Your approval rating is {approval}%, which is below the required 65%.")
        if not (1 <= inflation <= 5):
            print(f"- Your inflation rate is {inflation:.1f}%, which is outside the acceptable range of 1% to 5%.")
        if unemployment > 6:
            print(f"- Your unemployment rate is {unemployment:.1f}%, which is above the acceptable maximum of 6%.")
        print("Better luck next time!")

if __name__ == "__main__":
    main()
