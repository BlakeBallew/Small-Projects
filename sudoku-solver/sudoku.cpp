#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> collect_indices(int board[9][9])
{
    vector<vector<int>> indices = {};
    int x;
    for (x = 0; x < 9; x++)
    {
        int y;
        for (y = 0; y < 9; y++)
        {
            if (board[x][y] == 0)
            {
                indices.push_back({x, y});
            }
        }
    }
    return indices;
}

bool check_row(int board[9][9], int x, int y)
{
    int z;
    for (z = 0; z < 9; z++)
    {
        if (board[x][z] == board[x][y] && z != y)
        {
            return false;
        }
    }
    return true;
}

bool check_column(int board[9][9], int x, int y)
{
    int z;
    for (z = 0; z < 9; z++)
    {
        if (board[z][y] == board[x][y] && z != x)
        {
            return false;
        }
    }
    return true;
}

bool check_box(int board[9][9], int x, int y)
{
    int top_left_x = x - (x % 3);
    int top_left_y = y - (y % 3);
    int i;
    for (i = top_left_x; i < top_left_x + 3; i++)
    {
        int j;
        for (j = top_left_y; j < top_left_y + 3; j++)
        {
            if (board[i][j] == board[x][y] && i != x)
            {
                return false;
            }
        }
    }
    return true;
}

bool is_valid(int board[9][9], int x, int y)
{
    if (!(check_row(board, x, y) && check_column(board, x, y) && check_box(board, x, y)))
    {
        return false;
    }
    return true;
}

void solve(int board[9][9], vector<vector<int>> indices)
{
    int current_idx = 0;
    int length = indices.size();
    while (current_idx < length)
    {
        if (current_idx < 0)
        {
            cout << "Error: no solution" << endl;
            break;
        }

        bool flag = false;
        int current_x = indices.at(current_idx).at(0);
        int current_y = indices.at(current_idx).at(1);
        int current_on_board = board[current_x][current_y];

        int i;
        for (i = 1; i < 10; i++)
        {
            board[current_x][current_y] = i;
            if (is_valid(board, current_x, current_y) && i > current_on_board)
            {
                current_idx++;
                flag = true;
                break;
            }
        }

        if (!flag)
        {
            board[current_x][current_y] = 0;
            current_idx--;
        }
    }
}

void print_board(int board[9][9])
{
    int x;
    for (x = 0; x < 9; x++)
    {
        int y;
        for (y = 0; y < 9; y++)
        {
            cout << board[x][y] << " ";
        }
        cout << "" << endl;
    }
    cout << "" << endl;
}

int main()
{
    // test case: approx 55 million iterations to figure out this puzzle is invalid
    // runs in approx 13 seconds compared to python implementation which takes approx. 300 seconds
    int board[9][9] = {{0, 4, 3, 5, 2, 8, 0, 0, 0},
                       {2, 0, 0, 0, 9, 4, 0, 8, 0},
                       {0, 0, 0, 0, 0, 0, 0, 0, 0},
                       {0, 0, 0, 0, 0, 0, 0, 0, 0},
                       {0, 0, 9, 0, 1, 0, 0, 2, 4},
                       {7, 0, 0, 0, 4, 0, 0, 0, 0},
                       {0, 0, 0, 0, 0, 0, 0, 9, 6},
                       {0, 0, 0, 9, 7, 1, 0, 0, 0},
                       {6, 0, 0, 0, 8, 0, 0, 0, 0}};

    vector<vector<int>> indices = collect_indices(board);
    solve(board, indices);
    print_board(board);
}
