import tensorflow as tf

sess = tf.Session()

hello = tf.constant('Hello, TensorFlow!')
print sess.run(hello)

a = tf.constant(10)
b = tf.constant(32)
print sess.run(a + b)

a = tf.placeholder("float")
b = tf.placeholder("float")
y = tf.mul(a, b)
print sess.run(y, feed_dict={a: 3, b: 3})
