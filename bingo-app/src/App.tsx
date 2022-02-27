import { Card, Grid } from "@mui/material";
import { useState } from "react";

const activeColor = "lightgray";

interface BingoProps {
  number: number;
}

const BingoItem = (props: BingoProps) => {
  const [active, setActive] = useState(false);

  return (
    <Grid item xs={2}>
      <Card
        style={{ backgroundColor: active ? activeColor : "white" }}
        onClick={() => setActive(!active)}
      >
        <h1 style={{ textAlign: "center" }}>{props.number}</h1>
      </Card>
    </Grid>
  );
};

const CenterItem = () => {
  return (
    <Grid item xs={2}>
      <Card style={{ backgroundColor: activeColor }}>
        <h1 style={{ textAlign: "center" }}>X</h1>
      </Card>
    </Grid>
  );
};

function App() {
  const getNumbers = () => {
    var b: number[] = [];
    var i: number[] = [];
    var n: number[] = [];
    var g: number[] = [];
    var o: number[] = [];
    var bingo = [b, i, n, g, o];
    bingo.forEach((element, index) => {
      const min = index * 15 + 1;
      const max = (index + 1) * 15;

      while (element.length < 5) {
        const random = Math.floor(Math.random() * (max - min + 1)) + min;
        if (!element.includes(random)) {
          element.push(random);
        }
      }
    });

    console.log(bingo);
    return bingo;
  };

  const numbers = getNumbers();

  return (
    <Grid
      container
      spacing={2}
      style={{
        marginTop: 10,
      }}
    >
      <Grid item xs={1} />
      <BingoItem number={numbers[0][0]} />
      <BingoItem number={numbers[1][0]} />
      <BingoItem number={numbers[2][0]} />
      <BingoItem number={numbers[3][0]} />
      <BingoItem number={numbers[4][0]} />
      <Grid item xs={1} />

      <Grid item xs={1} />
      <BingoItem number={numbers[0][1]} />
      <BingoItem number={numbers[1][1]} />
      <BingoItem number={numbers[2][1]} />
      <BingoItem number={numbers[3][1]} />
      <BingoItem number={numbers[4][1]} />
      <Grid item xs={1} />

      <Grid item xs={1} />
      <BingoItem number={numbers[0][2]} />
      <BingoItem number={numbers[1][2]} />
      <CenterItem />
      <BingoItem number={numbers[3][2]} />
      <BingoItem number={numbers[4][2]} />
      <Grid item xs={1} />

      <Grid item xs={1} />
      <BingoItem number={numbers[0][3]} />
      <BingoItem number={numbers[1][3]} />
      <BingoItem number={numbers[2][3]} />
      <BingoItem number={numbers[3][3]} />
      <BingoItem number={numbers[4][3]} />
      <Grid item xs={1} />

      <Grid item xs={1} />
      <BingoItem number={numbers[0][4]} />
      <BingoItem number={numbers[1][4]} />
      <BingoItem number={numbers[2][4]} />
      <BingoItem number={numbers[3][4]} />
      <BingoItem number={numbers[4][4]} />
      <Grid item xs={1} />
    </Grid>
  );
}

export default App;
