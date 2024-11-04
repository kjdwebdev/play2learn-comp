<template>
    <p>This is the math game Vue.</p>
    <div>
        <div>
            <label for="user_id">User Id</label>
            <input name="user_id" type="number" id="user_id" v-model="user_id">
        </div>
        <div>
            <label for="score">Score</label>
            <input name="score" type="number" id="score" v-model="score">
        </div>
        <div>
            <label for="max_number">Max Number</label>
            <input name="max_number" type="number" id="max_number" v-model="max_number">
        </div>
        <div>
            <label for="operation" class="form-label col-3">Operation</label>
            <select id="operation" class="form-select col" v-model="operation">
              <option v-for="symbol, operation in operations" :key="operation" :value="symbol">
                {{ operation }}
              </option>
            </select>

        </div>
        <button @click="recordScore">Record Score</button>
    </div>
</template>

<script>

    export default{
        name: 'MathGame',
        data() {
            return{ 
                "current_user": 'me',
                "game": "MATH",
                "score": 0,
                "max_number": 30,
                "operation": '',
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
                    
                    "game": "MATH",
                    "score": this.score,
                    "max_number": this.max_number,
                    "operation": this.operation,
                    operations: {
                        "Addition": "+",
                        "Subtraction": "-",
                        "Multiplication": "x",
                        "Division": "/"
                    },
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