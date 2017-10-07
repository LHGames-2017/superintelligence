from abc import ABCMeta, abstractmethod

from ServerCommands import *


class PlayerState:
    """ Abstract class for player states """
    __metaclass__ = ABCMeta

    def doAction(self):
        raise NotImplementedError()

