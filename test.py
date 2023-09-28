# test

# height = [170, 180, 175, 160]
# shoe = [260, 270, 265, 255]

# a = tf.Variable(0.1)
# b = tf.Variable(0.2)

# def wf():
#   return tf.square(shoe - (height * a + b))

# opt = tf.keras.optimizers.Adam(learning_rate=0.01)

# for i in range(3000):
#   opt.minimize(wf,var_list=[a,b])
#   # print(i,a.numpy(),b.numpy())
#   if i ==2999:
#     print(160 * a.numpy() + b.numpy())