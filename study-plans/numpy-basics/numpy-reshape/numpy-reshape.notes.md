# For image



images = np.random.randn(100, 28, 28)         # (batch, height, width)

images_4d = images.reshape(100, 1, 28, 28)    # (batch, channels, height, width)

# or equivalently:

images_4d = images[:, np.newaxis, :, :]


## Common pitfall

Be careful for reshaping because the shape of the old vector and the new one must be the same