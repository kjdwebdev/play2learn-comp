<template>
    <p>This is the math game Vue.</p>
    <div class="col">
        <div class="row">
            <label for="user_id">User Id</label>
            <input name="user_id" type="number" id="user_id" v-model="user_id">
        </div>
        <div class="row">
            <label for="score" class="form-label col-3">Score</label>
            <input name="score" type="number" id="score" v-model="score">
        </div>
        <div class="row">
            <label for="operation" class="form-label col-3">Operation</label>
            <select id="operation" class="form-select col" v-model="operation">
              <option v-for="symbol, operation in operations" :key="operation" :value="symbol">
                {{ operation }}
              </option>
            </select>
        </div>
        <div class="row">
            <label for="max-number" class="form-label col-3">Max Number</label>
            <input id="max-number" class="form-control col" type="number" min="1" max="100" v-model="maxNumber">
        </div>
        <button @click="recordScore">Record Score</button>
    </div>
</template>

<script>
    export default{
        name: 'MathGame',
        data() {
            return{ 
                "game": "MATH",
                "score": 0,
                "maxNumber": 30,
                "operation": '+',
                operations: {
                    "Addition": "+",
                    "Subtraction": "-",
                    "Multiplication": "x",
                    "Division": "/"
                },
                "user_id": 0,
            }
        },
        methods: {
            async recordScore(){
                const data = {
                    //"user": 'me',
                    "game": "MATH",
                    "score": this.score,
                    "max_number": this.maxNumber,
                    "operation": this.operation,
                    "user_id": this.user_id
                };
                console.log(data);
                const response = (await this.axios.post("/record-score/", data)).data;
                console.log(response)

            }
        }
    }
</script>

<style scoped>
    div, label{
        padding: 0.2rem;
    }
</style>