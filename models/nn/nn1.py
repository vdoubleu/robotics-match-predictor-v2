import numpy as np
import tensorflow as tf

from make_frame import make_dataframe

"""
input: average wins and losses of team throughout most recent season
[red1_wins, red1_losses, red2_wins, red2_losses, blue1_wins, blue1_losses, blue2_wins, blue2_losses]

output: probability that either red or blue wins
[red_win, blue_win]
"""

#created a function to make creating layers a lil easier
def makeLayer(layer_in_val, layer_in_num, layer_num):
    w = tf.Variable(tf.random.normal([layer_in_num, layer_num]))
    b = tf.Variable(tf.random.normal([layer_num]))
    return tf.matmul(layer_in_val, w) + b

#number of input and output nodes
x_node_num = 8
y_node_num = 2

#number of nodes in hidden layers
hidden_node_num = [20, 40, 10]

#some more parameters
learn_rate = 0.1
reps = 10000
disp_num = 100

x = tf.compat.v1.placeholder("float", [None, x_node_num])
y = tf.compat.v1.placeholder("float", [None, y_node_num])

l1 = tf.nn.relu(makeLayer(x, x_node_num, hidden_node_num[0]))
l2 = tf.nn.relu(makeLayer(l1, hidden_node_num[0], hidden_node_num[1]))
l3 = tf.nn.relu(makeLayer(l2, hidden_node_num[1], hidden_node_num[2]))

y_out = makeLayer(l3, hidden_node_num[2], y_node_num) 
out = tf.nn.softmax(y_out)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y_out, labels=y))

optimiser = tf.compat.v1.train.AdamOptimizer(learning_rate=learn_rate).minimize(cost)

init = tf.initialize_all_variables()

sess = tf.compat.v1.Session()
sess.run(init)

df = make_dataframe()

for entry in range(df.index.stop):
    row = df.iloc[entry]
    
    x_in = np.array([[row["red1"]["wins"], row["red1"]["losses"], row["red2"]["wins"], row["red2"]["losses"], row["blue1"]["wins"], row["blue1"]["losses"], row["blue2"]["wins"], row["blue2"]["losses"]]])

    if row["redScore"] > row["blueScore"]:
        y_out = np.array([[1, 0]])
    else:
        y_out = np.array([[0, 1]])

    loss, acc = sess.run([optimiser, cost], feed_dict={x: x_in, y: y_out})

    if entry % disp_num == 0:
        print("step", entry, " Current cost:", acc)
        val = x_in
        
        res = sess.run(out, feed_dict={x: val})
        print(res)
        print(y_out)
