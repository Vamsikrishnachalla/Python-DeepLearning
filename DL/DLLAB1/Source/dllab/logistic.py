#  we are importing MINST dataset that containes hand written images.
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)


import tensorflow as tf

# various parameters that are needed to train the dataset.
lrate = 0.0001
trainiter = 40
bsize = 50
dstep = 1

# giving inputs to tensorflow
x = tf.placeholder("float", [None, 784]) # mnist data image of shape 28*28=784
y = tf.placeholder("float", [None, 10]) # 0-9 digits recognition => 10 classes

# Genrating the model
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# Constructing the logistic model
model = tf.nn.softmax(tf.matmul(x, W) + b) # Softmax

# Minimizing the error rate by using cross-entropy values.

cost_function = -tf.reduce_sum(y*tf.log(model))

# Gradient Descent optimizer implementation
optimizer = tf.train.GradientDescentOptimizer(lrate).minimize(cost_function)

# Initialize the variables.
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)

    writer = tf.summary.FileWriter('./graphs/logistic_reg', sess.graph)
    for iteration in range(trainiter):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples / bsize)
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(bsize)
            # Fit training using batch data
            sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
            # Compute average loss
            avg_cost += sess.run(cost_function, feed_dict={x: batch_xs, y: batch_ys})/total_batch
        # Display logs per eiteration step
        if iteration % dstep == 0:
            print ("epoch:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(avg_cost))

    writer.close()
    print ("Tuning completed!")


    predictions = tf.equal(tf.argmax(model, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(predictions, "float"))
print ("Accuracy:", accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))