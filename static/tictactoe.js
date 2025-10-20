const p1 = 1;
const p2 = -1;
const board = [0,0,0, 0,0,0, 0,0,0]

var isP1Turn = true;
var isGameOver = false;

var container = document.getElementById("container");
var resetBtn = document.getElementById("reset");
resetBtn.addEventListener('click', () => {
    reset();
});

var squares = container.getElementsByTagName("div")
for (let idx=0; idx<squares.length; idx++) {
    squares[idx].addEventListener("click", () => handleOnClick(idx))
}

const CheckGameOver = (idx) => {
    var areAllSquaresUsed = board.every(x => x != 0);

    var checkHorizontal = () => {
        var player = getPlayerValue();
        for (let idx=0; idx<=6; idx += 3) {
            if ([board[idx], board[idx+1], board[idx+2]].every(x => x === player)) {
                return true;
            }
        }
        return false;
    };

    var checkVertical = () => {
        var player = getPlayerValue();
        for (let idx=0; idx<=2; idx++) {
            if ([board[idx], board[idx+3], board[idx+6]].every(x => x === player)) {
                return true;
            }
        }
        return false;
    };

    var checkDiagonal = (idx) => {
        var toReturn = false;
        var player = getPlayerValue();
        var diags = [0,2,4,6,8];
        if (diags.includes(idx)) {
            toReturn = [board[0], board[4], board[8]].every(x => x === player) ||
            [board[2], board[4], board[6]].every(x => x === player);
        }
        return toReturn;
    };

    var isWinner =
        checkHorizontal(idx) ||
        checkVertical(idx) ||
        checkDiagonal(idx);
    markWinner(isWinner);
    isGameOver =  isWinner || areAllSquaresUsed
    return isGameOver;
}

var p1Wins = 0;
var p1WinsElement = document.getElementById("p1Wins");
var p2Wins = 0;
var p2WinsElement = document.getElementById("p2Wins");

const getPlayerValue = () => isP1Turn ? p1 : p2;
const getPlayerIcon = () => isP1Turn ? 'X' : 'O';

const markWinner = (isWinner) => {
    if (!isWinner) {
        return;
    }

    if (isP1Turn) {
        p1Wins++;
        p1WinsElement.innerText = p1Wins;
    } else {
        p2Wins++;
        p2WinsElement.innerText = p2Wins;
    }
}

const reset = () => {
    isGameOver = false;
    isP1Turn = true;
    for (let idx=0; idx<board.length; idx++) {
        board[idx] = 0;
        squares[idx].innerHTML = '';
    }
}

const handleOnClick = (idx) => {
    if (isGameOver) {
        return;
    }

    if (board[idx] === 0) {
        board[idx] = getPlayerValue();
        squares[idx].innerText = getPlayerIcon();

        CheckGameOver(idx)
        if (!isGameOver) {
            isP1Turn = !isP1Turn;
        }
    }
}
