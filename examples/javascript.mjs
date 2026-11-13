import { LichessClient } from "../javascript/src/index.js";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new LichessClient({ apiKey });

  const enums = await client.enums({  });
  console.log("enums", enums);
  const puzzleDaily = await client.puzzleDaily({  });
  console.log("puzzleDaily", puzzleDaily);
