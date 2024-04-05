class Lexicon:
    # General
    next = "Next"
    yes = "Yes"
    no = "No"

    # instruction_product
    product_intro_title = "Please read carefully: Instructions on the product choice task"
    product_intro_text1 = "In the upcoming pages, you will be presented with various hypothetical investment scenarios. <b>Please imagine that you are contemplating to purchase a new car.</b><br><br>"
    product_intro_text2 = "Your role is to evaluate different offers for <b>electric vehicles</b> and decide whether or not you would choose to buy each car. An electric car operates exclusively on electricity, utilizing an electric motor instead of the conventional internal combustion engine found in typical cars.<br><br>"
    product_intro_text3 = "Consider the following attributes that vary across the offers:"

    investment_cost = "Investment Costs:"
    savings = "Savings on Driving:"
    emissions = "Life Cycle Emissions:"
    range = "Battery Range:"
    adopters = "Adopters in the Neighborhood:"

    investment_cost_text = "This monetary attribute defines the <b>total investment costs of the electric car</b>. Citizens may be eligible for government subsidies, which reduce the costs. The costs depend on the make of the car and the subsidies received."
    savings_text = "Electric vehicles have lower running costs than traditional gasoline cars. The <b>savings are calculated compared to the costs of driving a gasoline car </b> and are based on electricity prices and efficiency for 100 miles."
    emissions_text = "This refers to the total greenhouse gas emissions associated with an electric vehicle <b>throughout its entire lifespan</b>. It takes into account emissions from manufacturing, disposal, and the electricity needed for the journey. In simpler terms, this corresponds to assessing the environmental footprint of the electric car from the moment of its creation to its retirement after <b>approximately 150,000 miles</b>."
    range_text = "Battery range indicates the <b>distance an electric vehicle can travel on a single battery charge</b>. It defines how far you can drive before needing to recharge the vehicle's battery."
    adopters_text = "This attribute represents the <b>percentage of people in your neighborhood who currently drive a <i>similar electric car</i></b>."

    product_intro_text4 = "Each electric car presented in an offer is designed to match the characteristics of a car you would consider buying. This includes factors such as model, size, engine power, and the number of doors."
    product_intro_text5 = "As in the practice run, the attributes of the products will be concealed behind boxes. To view the attributes, hover your mouse pointer over the box. The box will open, allowing you to see the information."
    product_intro_text6 = "Please decide whether you would or would not purchase each electric vehicle presented, considering that you need a new car. "

    # instruction_policy
    policy_intro_title = "Please read carefully: Instructions on the policy task"
    policy_intro_text1 = "In the following pages, we will present you with a series of hypothetical policy packages. The policies are designed to foster the uptake of electric vehicles. An electric car operates exclusively on electricity, utilizing an electric motor instead of the conventional internal combustion engine found in typical cars."
    policy_intro_text2 = "Your task is to evaluate and express your support or non-support for each policy proposal."
    policy_intro_text3 = "Each policy package will consist of different combinations of the following attributes:"

    tax = "Carbon Tax on Gasoline:"
    subsidy = "Subsidies on Investment Costs:"
    label = "Climate Label:"

    tax_text = "This attribute indicates whether the government proposes a <b>carbon tax on the emissions from gasoline</b> in $ per metric ton of CO2, which increases the fuel price. A carbon tax is a policy tool which discourages the use of fossil fuels and encourages a shift towards cleaner energy sources. In this context, it reflects a policy tool to stimulate the transition from traditional gasoline powered vehicles to cleaner alternatives such as electric vehicles."
    subsidy_text = "This attribute indicates whether there are <b>government subsidies (price reduction)</b> provided to individuals who buy an electric vehicle. Subsidies on investment costs are designed to make electric vehicles more financially attractive and affordable for consumers, promoting the adoption of electric cars. However, it's important to note that these subsidies might also mean that the funds are not available for other projects."
    label_text = "This attribute describes whether the government plans to introduce a <b>voluntary or mandatory climate label on cars</b> (or no label). The climate label provides information about <b>gasoline cars climate footprint compared to EVs</b> and the other way round. A voluntary or mandatory climate label is a policy tool to enhance consumer awareness and transparency regarding the environmental impact of vehicle choices."
    adopters_policy_text = "To evaluate the potential impact of a policy package, it is crucial to understand the number of people affected by the policy. This attribute indicates the <b>percentage of EVs among new car registrations in your neighborhood <i>over the last year</i></b>. Please make your decisions under the assumption that of all new car registrations in your area, the provided number of people has adopted an electric vehicle."

    policy_intro_text4 = "The different parts of the policy packages will be concealed behind boxes. To view the information, hover your mouse pointer over the box. The box will open, allowing you to see the information."
    policy_intro_text5 = "Please decide whether or not you would support each policy package presented."

    # TaskPage
    block_text_intro = "Please be aware of the following:"
    no_policies = "The previous government policies are no longer in effect."
    product_intro_short = "On the next pages, we ask you again to decide for or against electric vehicle offers. As before, please consider the following attributes that vary across the offers:"
    policy_change = "Please be aware of a recent government policy change:"

    policy_question = "Would you support this policy package?"
    product_question = "Would you buy this electric vehicle?"

    affirmative_text = 'Well done on completing the block!'
    # Add block-specific texts
    block_texts = {
        'A': '<br>A carbon tax on gasoline is now in effect. '
             'This tax increases the savings of an electric car compared to a gasoline car per 100 miles. '
             'Find the tax amount in the <b>Savings Compared to Gasoline Car</b> box. <br>',

        'B': '<br> '
             'A carbon tax on gasoline is now in effect. '
             'This tax increases the savings of electric cars compared to gasoline cars per 100 miles. '
             'Find the tax amount in the <b>Savings Compared to Gasoline Car</b> box. <br>'
             'Additionally, the government introduced a manufacturer label on cars. '
             'The greenhouse gas emissions information is presented as a percentage label. '
             'It reflects the <b>emission savings of electric vehicles compared to similar-sized gasoline cars '
             'over the whole lifespan of the car</b>. '
             'Find the label in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br>',

        'C': '',

        'D': '<br>'
             'The government introduced a manufacturer label on cars. '
             'The greenhouse gas emissions information is presented as a percentage label. '
             'It reflects the <b>emission savings of electric vehicles compared to similar-sized gasoline cars '
             'over the whole lifespan of the car</b>. '
             'Find the label in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br>',
    }

    policy_package_no = "Policy Package"
    product_offer_no = "Electric Vehicle Offer"
