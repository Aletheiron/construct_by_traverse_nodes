from numpy import random
import matplotlib.pyplot as plt
import random

''' Nodes are not functions, but high-level actions'''


class Place_Item ():
    
    def __init__(self, coordinates, item: str, position: str):
        
        self.coordinates=coordinates
        self.item=item
        self.position=position
    
    def _params(self):
        
        return ({self.item}, {self.position})
    
    def forward (self):
        
        return f'Item {self.item} is placed {self.position}, then previous detail'
    
    def gen_with_params (self):
        
        return f'Item {self.item} is placed {self.position}, then previous detail'

node_1=Place_Item(coordinates=(1,1), item='A',position='Up')
node_2=Place_Item(coordinates=(1,0), item='A',position='Down')
node_3=Place_Item(coordinates=(1,2), item='A',position='Right')
node_4=Place_Item(coordinates=(2,2), item='A',position='Left')

node_5=Place_Item(coordinates=(0,1), item='B',position='Up')
node_6=Place_Item(coordinates=(2,1), item='B',position='Down')
node_7=Place_Item(coordinates=(2,3), item='B',position='Right')
node_8=Place_Item(coordinates=(3,3), item='B',position='Left')

list_of_current_nodes=[node_1,node_2,node_3,node_4,node_5,node_6,node_7,node_8]

#Create string class

class String():
    
    def __init__(self, coordinates, UF_initial):
        self.coordinates=coordinates
        self.UF_string=[]
        self.Node_list_string=[]
        self.param_node_list=[]
        
        #Some inyternalization of utility function, doesn't matter now. Later it probably will has sense
        self.UF_max=UF_initial
        self.UF=UF_initial
    
    def append_UF(self):
        self.UF_string.append(self.UF)
    
    def append_Node_string(self, node):
        self.Node_list_string.append(node)
    
    def append_param_list (self, param):
        self.param_node_list.append(param)
        
    def pass_through_nodes(self, x):
        
        line=''
        for i in range(len(self.Node_list_string)):
            line=line+i.gen_with_params+' '
        
        return line



#Generate the next node function
def generate_line (current_coord, list_of_nodes: list):
    
    list_of_probs=[]
    list_of_distances=[]
    
    #compute distances for each node
    for i in range(len(list_of_nodes)):
        
        list_of_quasi_dist=[]
        for j in range(len(list_of_nodes[i].coordinates)):
            dist=(current_coord[j]-list_of_nodes[i].coordinates[j])
            distance=dist*dist
            list_of_quasi_dist.append(distance)
        
        big_distance=sum(list_of_quasi_dist)
        list_of_distances.append(big_distance)
    
    #compute quasi-probabilities from inverses of distances
    for k in range(len(list_of_distances)):
        
        #eliminating 100% probability of beign in the current node
        if list_of_distances[k]==0:
            inv_dist=0
        else:
            inv_dist=1/(list_of_distances[k])
            
        inv_total_dist=1/sum(list_of_distances)
        prob=inv_dist/inv_total_dist
        list_of_probs.append(prob)
    
    chosen_node=random.choices(list_of_nodes, weights=list_of_probs,k=1)[0]
    
    #Generating next node
    return chosen_node

#Exogeneous settings

EPOCH=20
alpha=1

UF_initial=0.0

UF_max=UF_initial

string=String((0,0),UF_initial=UF_initial)
string.append_UF()
print(string.UF_string[-1])

for epoch in range(EPOCH):
    

    node=generate_line(string.coordinates,list_of_nodes=list_of_current_nodes) #attraction-like choice 
    
    #print(node)
    
    #string.coordinates=node.coordinates
    
    
    print(node.forward()) #applying given function
    print("Type new Utility Function")
    #print(logits)
    UF=float(input())
    
    string.UF=UF+string.UF_string[-1]
    #print(UF)
    
    if string.UF>=string.UF_max*alpha:
        print('Oooohhhuuu!')
        string.coordinates=node.coordinates
        string.append_UF()
        string.append_Node_string(node=node)
        string.append_param_list(node._params())
        
        #Update coordinates of the string ? May be in general case is better. Should check
        #string.coordinates=node.coordinates
        
        #Update maximum of the utility function
        if string.UF>=string.UF_max*alpha:
            UF_max=string.UF
            string.UF_max=UF_max
            #print(UF_max)
        
        #preparings for further applying of the same function
        UFtry=[] 
        UFtry.append(-1e30)
        
        UFtry_count=0 #need for skipping very big while loops in case of very little gradual improvements of utility function
        
        #if utility function is still improving
        while string.UF>=UF_max*alpha and string.UF>UFtry[-1] and UFtry_count<=3:
            
            
            
            print(node.forward()) #applying given function
            print("Type new Utility Function")
            #print(logits)
            UF=float(input())
    
            string.UF=UF+string.UF_string[-1]
            
            if string.UF>=string.UF_max*alpha:
                
                print("Great")
                UFtry.append(string.UF_string[-1])
                UFtry_count+=1
                
                string.append_UF()
                string.append_Node_string(node=node)
                string.append_param_list(node._params())
                UF_max=string.UF
                string.UF_max=UF_max
                
            else:
                print("Noooo!")
                UFtry.append(1e10)
    else:
        print('Doooont')

#some information during training   
print(string.UF_string)
#print(string.Node_list_string[:5], string.Node_list_string[-5:])
print(string.param_node_list)

#Plot Utility Function
plt.plot(string.UF_string)
plt.show()