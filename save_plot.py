import matplotlib.pyplot as plt

# Example data: replace these with your actual training/validation accuracy lists
epochs = list(range(1, 31))
train_acc = [0.2855,0.3594,0.3643,0.4688,0.4447,0.3750,0.4701,0.5000,0.4958,0.5714,
             0.5136,0.5156,0.5296,0.5156,0.5431,0.5312,0.5585,0.4688,0.5717,0.6250,
             0.5893,0.7031,0.5904,0.6875,0.6142,0.5781,0.6183,0.6562,0.6271,0.6406]
val_acc   = [0.3319,0.3333,0.4285,0.4277,0.4618,0.4616,0.4825,0.4834,0.4983,0.4968,
             0.4978,0.4979,0.5096,0.5065,0.5166,0.5167,0.5303,0.5287,0.5366,0.5360,
             0.5532,0.5540,0.5530,0.5529,0.5507,0.5456,0.5470,0.5480,0.5604,0.5593]

plt.figure(figsize=(8,6))
plt.plot(epochs, train_acc, label='Training Accuracy')
plt.plot(epochs, val_acc, label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Over Epochs')
plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('accuracy_plot.png')
print("Plot saved as accuracy_plot.png")
