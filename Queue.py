################
# Python 3.5 File
# Group 1
# created oct. 24th 2018
# last modif oct. 24th 2018
# Queue.py
################

#Une file est une liste où les insertions se font d'un
#côté et les suppressions se font de l'autre côté

#[Lise]
#1- Est-ce qu'on est sûre que les valeurs stockées dans notre queue
# doivent obligatoirement être de type Int ? Pourquoi pas des Float ? ou Str ?
#[Morgane]
#Pour moi cela fait partie des consignes de l'énoncé,
#les graphes que l'ont parcours sont ceux déjà créés en cours, donc avec des sommets numérotés de 0 à n
#et l'on ne crée la classe file que pour cela, après je vérifie le type int pour être sure de n'ajouter que des sommets
#et pas autre chose (liste de sommet par exemple) par inadvertance

#2- J'ai un petit soucis avec les types des méthodes.
# Par exemple, pour getList() j'aurais indiqué:
#   """Queue -> List"""
# Est-ce que tu es d'accord ?
#[Morgane]
#Je viens de vérifier dans l'énoncé du projet, effectivement par exemple getLeftSon() prend un BinTree, je corrige

#3-Pour dequeue, est-ce qu'on autorise l'application de la méthode à une file vide ?
#[Morgane]
#A priori non, dans la consigne il est écrit " le premier élément d’une file non vide" pour peek,
#et en cours le prof nous a dit que les deux vont toujours ensemble normalement

#[Morgane] Je viens de remarquer que l'on a utilisé le mot clé list comme variable, histoire d'éviter tout pb, je rajoute un e

class Queue :

    def __init__(self, liste):
        """ The empty queue is the queue with [] argument """
        #assert isinstance(list, list)
        self.liste = liste

    def getList(self):
        """ Queue --> List """
        return self.liste

    def setList(self, value):
        """ Queue and List --> None """
        assert isinstance(value, list) #[Lise] j'aurais mis cette ligne de vérification
                                       #        dans la constructeur __init__ qu'en penses-tu ?
        self.liste = value              #[Morgane] J'avais eu un problème du genre, et le prof m'a dit de ne jamais le faire
                                        #parce qu'il semblerait que cela ralentisse beaucoup le code, donc je suis plutot contre

    def isEmpty(self):
        """ Queue --> Bool """
        if (self.getList() == []):
            return True
        else:
            return False

    def enqueue(self, value):
        """ Queue and Int --> None
        ----------------
        Add the value at the end (right side) of the queue """
        assert isinstance(value, int)
        liste = self.getList()
        liste = liste + [value]
        self.setList(liste)

    def dequeue(self):
        """ Queue --> None
         ----------------
        If the queue is not empty, removes the value at the beginning (left side) of the queue
        Else, nothing"""        #[Morgane] personnellement j'aurais carrement mis un assert, si on essaie d'enlever
                                #sans se rendre compte que le liste est vide, c'est qu'il y a un problème dans le code
        if not self.isEmpty():
            queue = self.getList()
            newQueue = queue[1:]       #[Morgane] il faut compter que cette opération à une complexité en O(n) et pas de 1
                                       #comme les autres opérations, es ce qu'il n'y aurait pas moyen de faire autrement ?
            self.setList(newQueue)

    def peek(self):
        """ Queue -> Int
        ---------------
        Peek the first element (on the left-hand side of the queue)"""
        assert(not self.isEmpty())
        liste = self.getList()
        return liste[0]

