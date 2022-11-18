import argpase
import wandb


def parse_args():
    argparser = argparse.ArgumentParser(description='Process hyper-parameters')
    arparser.add_argument("--a", type=int, default=1)
    args = argparser.parse_args()
    return vars(args)

if __name__ == '__main__':
    config = parse_args()
    with wandb.init(config=config):
        print(config)
        pass
