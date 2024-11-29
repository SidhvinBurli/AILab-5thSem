 
class KnowledgeBase:
    def __init__(self):
      
        self.facts = set()   
        self.rules = []      

    def add_fact(self, fact):
        
        self.facts.add(fact)

    def add_rule(self, condition, conclusion):
        
        self.rules.append((condition, conclusion))

    def forward_reasoning(self):
        """ Perform forward reasoning to derive new facts """
        new_facts = set(self.facts)
        while True:
            added = False
            for condition, conclusion in self.rules:
                if condition(self.facts):   
                    if conclusion not in self.facts:  
                        self.facts.add(conclusion)
                        new_facts.add(conclusion)
                        added = True
            if not added:
                break  
        return new_facts


def get_input():
    """ Function to get user input for facts and rules """
    kb = KnowledgeBase()
    
    print("Enter facts (type 'done' to finish):")
    while True:
        fact = input("Fact: ").strip()
        if fact.lower() == 'done':
            break
        kb.add_fact(fact)
    
    print("\nEnter rules (condition -> conclusion, type 'done' to finish):")
    while True:
        rule_input = input("Rule: ").strip()
        if rule_input.lower() == 'done':
            break
        
      
        if '->' in rule_input:
            condition, conclusion = rule_input.split('->')
            condition = condition.strip()
            conclusion = conclusion.strip()

             
            kb.add_rule(lambda facts: condition in facts, conclusion)
        else:
            print("Invalid rule format. Please enter in the form: condition -> conclusion")
    
    return kb


 
def main():
    print("Welcome to the Forward Reasoning System!\n")
    kb = get_input()

    
    kb.forward_reasoning()

    print("\nAll derived facts:")
    for fact in kb.facts:
        print(fact)

    
    query = input("\nEnter a query to check if it's a fact (e.g., HasLegs(John)): ").strip()
    
    if query in kb.facts:
        print(f"Yes, {query} is a fact.")
    else:
        print(f"No, {query} is not a fact.")


if __name__ == "__main__":
    main()
