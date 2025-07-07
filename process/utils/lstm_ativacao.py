import torch.nn as nn

class LSTMAtivacao(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size, ativacao):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, dropout=0.2)
        self.regressor = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            ativacao,
            nn.Linear(hidden_size, output_size)
        )

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.regressor(out[:, -1, :])