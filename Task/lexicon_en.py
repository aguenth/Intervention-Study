class Lexicon:
    # General
    next = "Next"
    yes = "Yes"
    no = "No"

    # instruction_product
    product_intro_title = "Please read carefully: Instructions on the product choice task"
    product_intro_text1 = "In the upcoming pages, you will be presented with various hypothetical investment scenarios. <b>Please imagine that you would like to purchase a new car.</b><br><br>"
    product_intro_text2 = "Your role is to evaluate different offers for <b>electric vehicles</b> and decide whether or not you would choose to buy each car. An electric car operates exclusively on electricity, utilizing an electric motor instead of the conventional internal combustion engine found in typical cars.<br><br>"
    product_intro_text3 = "Consider the following attributes that vary across the offers:"

    investment_cost = "<u>Investment Costs:</u>"
    savings = "<u>Savings on Driving:</u>"
    emissions = "<u>Life Cycle Emissions:</u>"
    range = "<u>Battery Range:</u>"
    adopters = "<u>Adopters in the Neighborhood:</u>"

    investment_cost_text = "This financial attribute shows the <b>net price of the electric car</b>. There are government subsidies that can reduce the price. The cost depends on the car brand and the subsidies/discounts subtracted."
    savings_text = "Charging an electric vehicles is <b>cheaper than fueling a gasoline car</b>. Therefore, the costs per mile are lower for electric vehicles than for gasoline cars. The savings are calculated by comparing electricity prices with gas prices and the efficiency of electric vehicles with traditional cars. <b>The value presented tells you how much you can save with this electric car for 100 miles.</b>"
    emissions_text = "The emissions show the environmental footprint of the electric car <b>in metric tons</b> from the production to its decommissioning after <b>approx. 150,000 miles</b>. This includes emissions from production, disposal and the electricity needed for driving."
    range_text = "The battery range indicates the <b>distance an electric vehicle can travel on a single battery charge</b>. It indicates how many miles you can drive before you have to stop to charge the battery."
    adopters_text = "This attribute represents the <b>percentage of people in your neighborhood who currently drive a <i>similar</i> electric car</b>."

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

    tax_text = "The policy package can include a <b>carbon tax on gasoline emissions</b>. This tax is expressed in $ per metric ton of CO2. Each gallon of gasoline burned produces about 9 kilograms of CO2, so the carbon tax would increase the price of fuel. As a result, the savings from driving an electric vehicle would be higher compared to a gasoline car. The tax revenue would be redistributed to low-income households so that those who cannot afford an electric vehicle but have to rely on their car are not disadvantaged."
    subsidy_text = "This attribute indicates whether there are <b>government subsidies (price discounts)</b> provided to individuals who buy an electric vehicle. Subsidies on investment costs are designed to make electric vehicles more financially attractive and affordable for consumers, promoting the adoption of electric cars. However, it's important to note that these subsidies might also mean that the funds are not available for other projects."
    label_text = "This attribute describes whether the government plans to introduce a <b>voluntary or mandatory climate label for cars</b>. The climate label provides information about the <b>climate footprint of electric vehicles compared to gasoline vehicles</b> and vice versa (i.e. how much less emissions an electric car produces). A climate label is a policy tool to improve consumer awareness and transparency regarding the environmental impact of vehicle choices."
    adopters_policy_text = "To assess the potential impact of a package of measures, it is important to know the number of people affected by the measure. This attribute indicates the <b>percentage of electric vehicles among new registrations <i>in the last year</i></b>. Please make your decisions based on the assumption that of all new registrations in your region, the specified number of people have purchased an electric vehicle."

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

    BD1 = """Please consider for the next car offers that the government introduced a <b>manufacturer climate footprint label</b>. This label shows how much greenhouse gas emissions cars produce and in particular <b>how much emissions an electric car saves compared to a gasoline car in %</b>. You can find the label of each electric vehicle in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br><br>
    In addition, the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br>"""

    BD19 = """Please consider for the next car offers that there is <b>still the manufacturer climate footprint label</b> which shows <b>how much emissions an electric car saves compared to a gasoline car in %</b>. You can find the label of each electric vehicle in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br><br>
    There is <b>no gasoline tax for the next offers</b>. This means that the electric vehicles are still cost-effective compared to gasoline cars, but the savings are no longer increased by a higher gasoline price.<br>"""

    DB1 = """Please consider for the next car offers that the government introduced a <b>manufacturer climate footprint label</b>. This label shows how much greenhouse gas emissions cars produce and in particular <b>how much emissions an electric car saves compared to a gasoline car in %</b>. You can find the label of each electric vehicle in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br>"""

    DB19 = """Please consider for the next car offers that <b>in addition to the manufacturer climate footprint label</b> the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br><br>
    The climate label of each vehicle can again be found in the <b>Lifecycle Greenhouse Gas Emissions</b> box.<br>"""

    AC1 = """Please consider for the next car offers that the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br> """

    AC19 = """Please consider for the next car offers that there is <b>no gasoline tax. This means that the electric vehicles are still cost-effective compared to gasoline cars, but the savings are no longer increased by a higher gasoline price.<br>"""

    CA1 = """ """

    CA19 = """Please consider for the next car offers that the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br>"""

    BD37 = """Please consider for the next car offers that the government introduced a <b>manufacturer climate footprint label</b>. This label shows how much greenhouse gas emissions cars produce and in particular <b>how much emissions an electric car saves compared to a gasoline car in %</b>. You can find the label of each electric vehicle in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br><br>
    In addition, the government introduced a <b>price on the emissions from gasoline</b>. As before, this tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br>"""

    BD55 = """Please consider for the next car offers that there is <b>still the manufacturer climate footprint label</b> which shows <b>how much emissions an electric car saves compared to a gasoline car in %</b>. You can find the label of each electric vehicle in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br><br>
    There is <b>no gasoline tax for the next offers</b>. This means that the electric vehicles are still cost-effective compared to gasoline cars, but the savings are no longer increased by a higher gasoline price.<br>"""

    DB37 = """Please consider for the next car offers that the government introduced a <b>manufacturer climate footprint label</b>. This label shows how much greenhouse gas emissions cars produce and in particular <b>how much emissions an electric car saves compared to a gasoline car in %</b>. You can find the label of each electric vehicle in the <b>Lifecycle Greenhouse Gas Emissions</b> box. <br><br>"""

    DB55 = """Please consider for the next car offers that <b>in addition to the manufacturer climate footprint label</b> the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br><br>
    The climate label of each vehicle can again be found in the <b>Lifecycle Greenhouse Gas Emissions</b> box.<br>"""

    AC37 = """Please consider for the next car offers that there is <b>no manufacturer climate footprint label anymore</b>. But the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br>"""

    AC55 = """Please consider for the next car offers that there is <b>no manufacturer climate footprint label and no gasoline tax anymore</b><br>"""

    CA37 = """Please consider for the next car offers that there is <b>no manufacturer climate footprint label anymore</b>.<br>"""

    CA55 = """Please consider for the next car offers that there is still <b>no manufacturer climate footprint label</b>. But the government introduced a <b>price on the emissions from gasoline</b>. This tax means that the price per gallon of gasoline will increase. Depending on the level set by the government, this increase could be <b>around $0.5 per gallon or around $2. </b>Essentially, driving a gasoline vehicle will become more expensive, making <b>electric vehicles even more cost-effective.</b> To see how much you can save per 100 miles by choosing an electric vehicle, including the savings due to the carbon pricing, see the <b>Savings Compared to Gasoline Car</b> box.<br>"""

    policy_package_no = "Policy Package"
    product_offer_no = "Electric Vehicle Offer"
