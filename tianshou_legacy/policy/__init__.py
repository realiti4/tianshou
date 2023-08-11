from tianshou_legacy.policy.base import BasePolicy
from tianshou_legacy.policy.random import RandomPolicy
from tianshou_legacy.policy.modelfree.dqn import DQNPolicy
from tianshou_legacy.policy.modelfree.c51 import C51Policy
from tianshou_legacy.policy.modelfree.qrdqn import QRDQNPolicy
from tianshou_legacy.policy.modelfree.pg import PGPolicy
from tianshou_legacy.policy.modelfree.a2c import A2CPolicy
from tianshou_legacy.policy.modelfree.npg import NPGPolicy
from tianshou_legacy.policy.modelfree.ddpg import DDPGPolicy
from tianshou_legacy.policy.modelfree.ppo import PPOPolicy
from tianshou_legacy.policy.modelfree.trpo import TRPOPolicy
from tianshou_legacy.policy.modelfree.td3 import TD3Policy
from tianshou_legacy.policy.modelfree.sac import SACPolicy
from tianshou_legacy.policy.modelfree.discrete_sac import DiscreteSACPolicy
from tianshou_legacy.policy.imitation.base import ImitationPolicy
from tianshou_legacy.policy.imitation.discrete_bcq import DiscreteBCQPolicy
from tianshou_legacy.policy.modelbased.psrl import PSRLPolicy
from tianshou_legacy.policy.multiagent.mapolicy import MultiAgentPolicyManager


__all__ = [
    "BasePolicy",
    "RandomPolicy",
    "DQNPolicy",
    "C51Policy",
    "QRDQNPolicy",
    "PGPolicy",
    "A2CPolicy",
    "NPGPolicy",
    "DDPGPolicy",
    "PPOPolicy",
    "TRPOPolicy",
    "TD3Policy",
    "SACPolicy",
    "DiscreteSACPolicy",
    "ImitationPolicy",
    "DiscreteBCQPolicy",
    "PSRLPolicy",
    "MultiAgentPolicyManager",
]
