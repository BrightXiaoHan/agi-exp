from . import agi_exp_main_group as main_group

__all__ = ["rlhf"]


@main_group.group()
def rlhf():
    pass


@rlhf.command()
def train_reward_model():
    pass


@rlhf.command()
def train():
    train_reward_model()


@rlhf.command()
def predict():
    pass
