"""
Conflict Resolution
===================
Section 11

Demonstrates conflict resolution: voting, priority-based,
and consensus mechanisms.

How to run:
    python example.py

No external dependencies required (uses Python standard library only).
"""

import random

print("=" * 60)
print("CONFLICT RESOLUTION")
print("=" * 60)

# 1. Voting Mechanism
print("\n1. MAJORITY VOTING")
print("-" * 40)

class VotingSystem:
    def __init__(self):
        self.votes = {}
    def cast_vote(self, agent, choice):
        self.votes[agent] = choice
        print(f"  {agent:12s} votes for: {choice}")
    def resolve(self):
        from collections import Counter
        counts = Counter(self.votes.values())
        winner = counts.most_common(1)[0]
        print(f"  Result: '{winner[0]}' wins with {winner[1]}/{len(self.votes)} votes")
        return winner[0]

vote = VotingSystem()
random.seed(42)
options = ["Plan A: Deploy to AWS", "Plan B: Deploy to GCP", "Plan C: Deploy to Azure"]
agents = ["Architect", "DevOps", "CTO", "Security", "Developer"]

for agent in agents:
    choice = random.choice(options)
    vote.cast_vote(agent, choice.split(":")[0])

print()
vote.resolve()

# 2. Priority-Based Resolution
print("\n2. PRIORITY-BASED")
print("-" * 40)

class PriorityResolver:
    def __init__(self):
        self.proposals = []
    def add_proposal(self, agent, proposal, priority):
        self.proposals.append({"agent": agent, "proposal": proposal, "priority": priority})
    def resolve(self):
        sorted_p = sorted(self.proposals, key=lambda x: -x["priority"])
        print(f"  Proposals (by priority):")
        for p in sorted_p:
            print(f"    P{p['priority']}: [{p['agent']}] {p['proposal']}")
        winner = sorted_p[0]
        print(f"  Winner: {winner['agent']}'s proposal (priority={winner['priority']})")
        return winner

resolver = PriorityResolver()
resolver.add_proposal("Security", "Use encryption at rest", 9)
resolver.add_proposal("DevOps", "Use container orchestration", 7)
resolver.add_proposal("Developer", "Use serverless functions", 5)
resolver.resolve()

# 3. Consensus
print("\n3. CONSENSUS BUILDING")
print("-" * 40)

class ConsensusBuilder:
    def __init__(self, threshold=0.66):
        self.threshold = threshold
        self.opinions = {}
    def submit(self, agent, score):
        self.opinions[agent] = score
    def check_consensus(self, proposal):
        avg = sum(self.opinions.values()) / len(self.opinions)
        agreement = sum(1 for s in self.opinions.values() if s >= 0.5) / len(self.opinions)
        print(f"  Proposal: {proposal}")
        print(f"  Average score: {avg:.2f}, Agreement: {agreement:.0%}")
        if agreement >= self.threshold:
            print(f"  CONSENSUS REACHED (>= {self.threshold:.0%})")
        else:
            print(f"  NO CONSENSUS (< {self.threshold:.0%})")
        return agreement >= self.threshold

consensus = ConsensusBuilder()
consensus.submit("Agent-A", 0.8)
consensus.submit("Agent-B", 0.7)
consensus.submit("Agent-C", 0.9)
consensus.submit("Agent-D", 0.3)
consensus.check_consensus("Deploy microservices architecture")

print("\nDone!")
