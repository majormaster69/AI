male(champaklal).
male(kakubhai).
male(rupesh).
male(hrishikesh).
male(divyesh).
male(harshil).
male(swapnil).
female(heena).
female(kishori).
female(leena).
female(parul).
female(falguni).

parent(heena,leena).
parent(heena,parul).
parent(champaklal,leena).
parent(champaklal,parul).
parent(kishori,rupesh).
parent(kishori,hrishikesh).
parent(kakubhai,rupesh).
parent(kakubhai,hrishikesh).
parent(falguni,swapnil).
parent(hrishikesh,swapnil).
parent(rupesh,divyesh).
parent(rupesh,harshil).
parent(parul,divyesh).
parent(parul,harshil).

mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).

grandparent(X,Z):-parent(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
grandmother(X,Z):-mother(X,Y),parent(Y,Z).

sibling(X,Y):-father(Z,X),father(Z,Y),X\=Y.
brother(X,Y):-sibling(X,Y),male(X),X\=Y.
sister(X,Y):-sibling(X,Y),female(X),X\=Y.

uncle(X,Z):-parent(Y,Z),brother(X,Y).
aunt(X,Z):-parent(Y,Z),sister(X,Y).

cousin(Child1,Child2):-parent(Y1,Child1),parent(Y2,Child2),sibling(Y1,Y2).