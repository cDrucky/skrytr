import pyDatalog

# Define the pyDatalog terms
pyDatalog.Logic('X, Y, Z, economy, situation, country, stock, market, loss, company, people, labor_cost')

# Define the summarize predicate using <<
summarize = pyDatalog.Logic() << ("economy" == True) & ("situation" == True) & ("country" == True) & ("stock" == True) & ("market" == True) & ("loss" == True) & ("company" == True) & ("people" == True) & ("labor_cost" == True)

# Define the summary sentence
summary_sentence = "The country's economic situation is on edge due to the stock market crash, causing loss for many people."

# Convert the summary sentence to a pyDatalog query
summary_query = summary_sentence.replace('The ', '').replace(' is ', '(').replace(' due to the ', ', ').replace(', causing ', ', ') + ')'

# Evaluate the query and print the result
result = pyDatalog.ask(summary_query)
print(result)
