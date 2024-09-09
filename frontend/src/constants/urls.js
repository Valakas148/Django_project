const baseURL = '/api'

const auth = 'auth'
const announcements = 'announcements'
const cars = 'cars'
const models = 'models'
const brands = 'brands'
const users = 'users'

const urls = {
    auth:{
        login: auth,
        socket:`${auth}/token`
    },
    cars: {
        brands: `${cars}/${brands}`,
        models: `${cars}/${models}`
    },
    announcements,
    users,
}


export {
    baseURL,
    urls
}