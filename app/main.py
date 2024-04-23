from main.comprehension.comprehension_agent import ComprehensionAgent
from main.orchestration.orchestrator import Orchestrator
from main.reasoning.reasoning_agent import ReasoningAgent
from main.evaluation.evaluator import Evaluator

print('Cognitive CORE - Initializing...')

def main():
    print('Cognitive Core - Starting...')

def process_user_input(user_input: str) -> str:
    # Initialize system components
    comprehension = ComprehensionAgent()
    orchestrator = Orchestrator()
    reasoning = ReasoningAgent()
    evaluator = Evaluator()

    structured_input = comprehension.process_input(user_input)
    task = orchestrator.delegate_task(structured_input)
    solution = reasoning.solve(task)
    evaluation = evaluator.evaluate(solution)

    return evaluation

if __name__ == "__main__":
    main()
