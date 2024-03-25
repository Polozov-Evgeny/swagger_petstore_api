class UserEndpoints:
    CREATE_USER_EP = '/user'
    GET_USER_EP = '/user/{username}'
    UPDATE_USER_EP = '/user/{username}'
    DELETE_USER_EP = '/user/{username}'


class OrderEndpoints:
    CREATE_ORDER_EP = '/store/order'
    GET_ORDER_ER = '/store/order/{id}'
    DELETE_ORDER_EP = '/store/order/{id}'


class PetEndpoints:
    CREATE_PET_EP = '/pet'
    GET_PET_BY_STATUS_EP = '/pet/findByStatus'
    GET_PET_BY_ID_EP = '/pet/{petId}'
    UPDATE_PET_BY_ID_EP = '/pet/{petId}'
    DELETE_PET_EP = '/pet/{petId}'
