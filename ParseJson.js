const fs = require('fs')


function parseIntoJSON(jsonData){
    return JSON.parse(jsonData)
}

function read_and_parse(){
    return new Promise((res, rej)=>{
        fs.readFile('countries.json', 'utf-8', (err, data)=>{
            if(err){
                rej(err)
            }else{
                const parsedData = parseIntoJSON(data)
                res(parsedData)
            }
        })
    })
}



read_and_parse()
.then(data=>{
    console.log(data);
})
.catch(err=>{
    console.error(err)
})

