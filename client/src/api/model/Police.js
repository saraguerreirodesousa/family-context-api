/**
 * Family Context
 * This is the *DRAFT / WORK IN PROGRESS* API definition for Family Context. This document is currently undergoing rapid change and should not be used as basis for implementation without discussing with the project team. 
 *
 * OpenAPI spec version: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Contact from './Contact';
import OffenceSummary from './OffenceSummary';

/**
* The Police model module.
* @module model/Police
* @version 0.0.1
*/
export default class Police {
    /**
    * Constructs a new <code>Police</code>.
    * @alias module:model/Police
    * @class
    */

    constructor() {
                
    }

    /**
    * Constructs a <code>Police</code> from a plain JavaScript object, optionally creating a new instance.
    * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
    * @param {Object} data The plain JavaScript object bearing properties of interest.
    * @param {module:model/Police} obj Optional instance to populate.
    * @return {module:model/Police} The populated <code>Police</code> instance.
    */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Police();
                                    if (data.hasOwnProperty('serviceInvolvement')) {
                obj['serviceInvolvement'] = ApiClient.convertToType(data['serviceInvolvement'], 'String');
            }
            if (data.hasOwnProperty('contact')) {
                obj['contact'] = Contact.constructFromObject(data['contact']);
            }
            if (data.hasOwnProperty('policeStation')) {
                obj['policeStation'] = ApiClient.convertToType(data['policeStation'], 'String');
            }
            if (data.hasOwnProperty('offences')) {
                obj['offences'] = ApiClient.convertToType(data['offences'], [OffenceSummary]);
            }
        }
        return obj;
    }

    /**
    * @member {String} serviceInvolvement
    */
    serviceInvolvement = undefined;
    /**
    * @member {module:model/Contact} contact
    */
    contact = undefined;
    /**
    * @member {String} policeStation
    */
    policeStation = undefined;
    /**
    * @member {Array.<module:model/OffenceSummary>} offences
    */
    offences = undefined;




}
