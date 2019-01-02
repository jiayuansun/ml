import matplotlib.pyplot as plt 
from matplotlib import style
import numpy as np 
style.use('ggplot')

class Support_Vector_Machine:
    def __init__(self,visualization=True):
        self.visualization=visualization
        self.colors={1:'r',-1:'b'}
        if self.visualization:
            self.fig=plt.figure()
            self.ax=self.fig.add_subplot(1,1,1)
    #train by the data
    def fit(self,data):
        self.data=data
        
        #{||w||:[w,b]}
        #yi(xi*m+b)>=1
        opt_dict={}


        transforms=[[1,1],
                    [-1,1],
                    [-1,-1],
                    [1,-1]]
        all_data=[]
        for yi in self.data: #yi is -1 or 1 , the classification
            for featureset in self.data[yi]:
                for feature in featureset:
                    print(feature)
                    all_data.append(feature)
        self.max_feature_value=max(all_data) #all data is all the features
        self.min_feature_value=min(all_data)
        # print(self.max_feature_value,self.min_feature_value)
        all_data=None
        step_sizes=[self.max_feature_value*0.1,
                    self.max_feature_value*0.01,
                    #point of expense:
                    self.max_feature_value*0.001]
        
        #extremely expensive
        b_range_multiple=2

        #we dont need to take as small of steps
        #with b as we do w
        b_multiple=5
        #first 
        latest_optimum=self.max_feature_value*10

        for step in step_sizes:
            w=np.array([latest_optimum,latest_optimum])
            #we can do this because convex
            optimized=False
            while not optimized:
                for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                    self.max_feature_value*b_range_multiple,
                                    step*b_multiple):
                    for transformation in transforms:
                        w_t=w*transformation
                        #print('w_t:{}'.format(w_t))
                        found_option=True
                        #weakest link in the SVM fundamentially
                        #SMO attempts to fix this a bit
                        #yi(xi.w_b)>=1
                        #### add a break here later..
                        for i in self.data:
                            for xi in self.data[i]:
                                yi=i #yi is the features
                                if not yi*(np.dot(w_t,xi)+b)>=1:
                                    found_option=False
                                #print(xi,':',yi*(np.dot(w_t,xi)+b))
                                    #break
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)]=[w_t,b] #norm get the length of the vector
                if w[0]<0: #why stop at this
                    optimized=True
                    print('Optimized a step')
                else:
                    #w=[5,5]
                    #step=1
                    #w-[step,step]=[4,4]
                    w=w-step
                #opt_dict is all the magnitude ||w||:[w,b]
                norms=sorted([n for n in opt_dict])
                opt_choice=opt_dict[norms[0]]
                print(opt_choice)
                self.w=opt_choice[0]
                self.b=opt_choice[1]
                latest_optimum=opt_choice[0][0]+step*2
        for i in self.data:
            for xi in self.data[i]:
                yi=i
                print(xi,':',yi*(np.dot(self.w,xi)+self.b))


    def predict(self,features):
        #sign(x.w+b)
        classification=np.sign(np.dot(np.array(features),self.w)+self.b)
        if classification!=0 and self.visualization:
            self.ax.scatter(features[0],features[1],s=200,marker='*',c=self.colors[classification])
        return classification
    def visualize(self):
        [[self.ax.scatter(x[0],x[1],s=100 ,color=self.colors[i]) for x in data_dict[i]] for i in data_dict]

    #hyperplane=x.w+b
    #
        def hyperplane(x,w,b,v):
            return (-w[0]*x-b+v)/w[1]

        datarange=(self.min_feature_value*0.9,self.max_feature_value*1.1)
        hyp_x_min=datarange[0]
        hyp_x_max=datarange[1]

        #(w.x+b)=1
        #

        psv1=hyperplane(hyp_x_min,self.w,self.b,1) #y
        psv2=hyperplane(hyp_x_max,self.w,self.b,1)
        self.ax.plot([hyp_x_min,hyp_x_max],[psv1,psv2],"k")

        nsv1=hyperplane(hyp_x_min,self.w,self.b,-1) #y
        nsv2=hyperplane(hyp_x_max,self.w,self.b,-1)
        self.ax.plot([hyp_x_min,hyp_x_max],[nsv1,nsv2],"k")

        db1=hyperplane(hyp_x_min,self.w,self.b,0) #decision boundary
        db2=hyperplane(hyp_x_max,self.w,self.b,0)
        self.ax.plot([hyp_x_min,hyp_x_max],[db1,db2],'g--')  

        plt.show()      

data_dict={-1:np.array([[1,7],
                        [2,8],
                        [3,8],]),
            1:np.array([[5,1],
                        [6,-1],
                        [7,3],])
                        
                        }


svm=Support_Vector_Machine()
svm.fit(data=data_dict)

predict_us = [[0,10],
              [1,3],
              [3,4],
              [3,5],
              [5,5],
              [5,6],
              [6,-5],
              [5,8]]

for p in predict_us:
    svm.predict(p)

svm.visualize()

